#chatbot 
# Nmrecassistant: A Flask-based PDF Link Retrieval Chatbot

This repository contains the code for Nmrecassistant, a simple chatbot built using Flask that allows users to retrieve PDF links based on their queries about departments, semesters, and subjects. 

## Features

- **User-friendly interface:** Interacts with users through a simple chat interface.
- **JSON-based data:** Uses JSON files to store data about departments, subjects, and associated PDF links.
- **Dynamic PDF link retrieval:** Retrieves the relevant PDF link based on user input.
- **Error handling:** Handles potential errors during data loading and PDF link retrieval.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Nmrecassistant.git
   pip install -r requirements.txt

##Configure Json data

Edit the data/departments.json, data/subjects.json, and data/pdf_paths.json files to populate the data with your desired department, subject, and PDF link information.
Ensure that the PDF files are stored in the static folder of the project.

This will start the server, and you can access the chatbot at http://127.0.0.1:5000/ or http://127.0.0.1:5000/home.

##Usage
Access the Chatbot: Open the chatbot interface in your web browser at the URL provided when you run the server.
Input Information: Type your request, specifying the department, semester, and subject. For example:
"Computer Science Semester 2 Data Structures"
"Electrical Engineering Semester 4 Circuit Theory"
Retrieve PDF Link: The chatbot will search for the corresponding PDF link and provide a clickable link if found.
##Code Structure

The main components of the project are:
app.py: Contains the Flask application code, including routes, chatbot logic, and data loading.
templates/index.html: Defines the front-end structure of the chatbot interface.
data/: Contains JSON files for departments, subjects, and PDF paths.
static/: Stores the PDF files for past papers.

##Future Improvements
Advanced Chatbot Logic: Implement more sophisticated natural language processing techniques for better understanding of user queries.
Database Integration: Store data in a database for better scalability and data management.
User Authentication: Implement user authentication to provide personalized access to PDFs.
Search Functionality: Allow users to search for PDFs using keywords or filters.

##Contribution
Contributions are welcome! Please open an issue or submit a pull request for any bug fixes or enhancements.

