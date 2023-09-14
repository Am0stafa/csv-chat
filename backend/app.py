import os
from dotenv import load_dotenv
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from flask import Flask, jsonify, request
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY must be set in .env file")

# setup the route
@app.route('/predict', methods=['POST'])
def predict():
    # get the file that was uploaded
    file = request.files['file']
    # save the file to local filesystem to be able to read it
    file.save(file.filename)
    #define the agent which under the hood uses the OpenAI to interpret the csv
    agent = create_csv_agent(OpenAI(api_key=openai_api_key, temperature=0.2), file.filename, verbose=True)
    print(agent.agent.llm_chain.prompt.template)
    # get the question from the request
    question = request.form['question']
    # find the result based on the question
    result = agent.run(question)
    os.remove(file.filename)
    return jsonify({'result': result})

if __name__ == '__main__':
  app.run(debug=True)
