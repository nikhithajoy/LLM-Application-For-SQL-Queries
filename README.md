# LLM-Application-For-SQL-Queries

This project utilizes Google's GenerativeAI (Gemini) model along with SQLite to create an interactive Streamlit application that generates and executes SQL queries based on user-provided questions.

## Overview
The Gemini SQL Query Generator is designed to demonstrate the use of natural language processing (NLP) techniques to interpret user questions and generate corresponding SQL queries to retrieve data from a SQLite database. The application leverages the following key components:

1. Google GenerativeAI (Gemini): The GenerativeAI model is used to understand user queries and prompts, generating SQL-like responses that can be executed against the database.

2. SQLite Database: The project includes a SQLite database (student.db) containing sample student data. The generated SQL queries are executed against this database to retrieve information based on user queries.

3. Streamlit: The interactive web application is built using Streamlit, allowing users to input questions and view the results of the generated SQL queries in real-time.

## Features
* User-friendly interface for entering natural language questions related to the database content.
* Integration with Google's GenerativeAI model for converting questions into SQL-like queries.
* Execution of generated SQL queries against a SQLite database to retrieve relevant information.
* Display of query results within the Streamlit application interface.

## Usage
To run the application locally:

1. Clone the repository to your local machine.
2. Install the required Python packages using pip install -r requirements.txt.
3. Ensure you have set up the necessary environment variables, including GOOGLE_API_KEY for accessing the GenerativeAI model.
4. Run streamlit run sql.py in your terminal to start the Streamlit application.
5. Input questions in natural language and click "Ask the question" to generate and execute SQL queries.

## Dependencies
* Python 3.x
* Streamlit
* SQLite3
* dotenv (for managing environment variables)
* google.generativeai (for accessing the GenerativeAI model)
