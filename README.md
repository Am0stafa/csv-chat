# CSV Chat App with Langchain and ChatGPT API

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup and Installation](#setup-and-installation)
- [Running the App](#running-the-app)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [How to Use](#how-to-use)
- [Technologies Used](#technologies-used)

## Overview

This is a simple chat application that allows users to upload a CSV file and ask questions about its content. It utilizes Langchain to interpret the CSV file and ChatGPT API to answer the questions.

The project consists of two main components:

- **Backend**: A Flask application that handles file uploads and interfaces with Langchain and ChatGPT API to interpret and answer questions about the CSV data.
- **Frontend**: A React Native application that provides a simple UI for users to upload a CSV file and input a question.

## Getting Started

### Prerequisites

1. **Python 3.x**
2. **Node.js**
3. **Yarn or npm**

### Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Am0stafa/csv-chat.git
   ```
2. **Navigate into the backend directory and install Python dependencies**
   ```bash
cd backend
pip install -r requirements.txt
    ```
3. **Add in the .env file with the openAI ket**
    ```bash
  OPENAI_API_KEY=your-openai-api-key

    ```
4. **Navigate into the frontend directory and install Node dependencies**
    ```bash
cd frontend
npm install
    ```
  