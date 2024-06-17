from flask import Flask, render_template, request, jsonify, url_for
import json

app = Flask(__name__)

# Load JSON files with error handling
def load_json_file(file_path):
    data = {}
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file {file_path}: {str(e)}")
    return data

# Define paths to JSON files
departments_path = 'data/departments.json'
subjects_path = 'data/subjects.json'
pdf_paths_path = 'data/pdf_paths.json'

# Load JSON files
departments_data = load_json_file(departments_path)
subjects_data = load_json_file(subjects_path)
pdf_links_data = load_json_file(pdf_paths_path)

# Serve the index.html file as the main page
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['userInput']

    # Implement chatbot logic here using the loaded JSON data
    response = handle_user_input(user_input)

    return jsonify({'botResponse': response})

def handle_user_input(user_input):
    input_lower = user_input.lower()
    response = ''
    if 'hi' in input_lower or 'hello' in input_lower:
        response = 'Hello! How can I assist you today?'
        return response
    if 'what is your name' in input_lower or 'what"s your name' in input_lower:
        response = 'my name Nmrecassistant,i can help or previous papers pdf links provided?'
        return response


    # Example logic: Retrieve PDF links based on user input
    for dept, dept_name in departments_data.items():
        if dept in input_lower:
            for sem, subjects in subjects_data.get(dept, {}).items():
                if sem in input_lower:
                    for subject in subjects:
                        if subject in input_lower:
                            pdf_link = pdf_links_data.get(dept, {}).get(sem, {}).get(subject)
                            if pdf_link:
                                pdf_url = url_for('static', filename=pdf_link)
                                response = f"Here is the PDF for {subject} ({dept_name} {sem}): <a href='{pdf_url}' target='_blank'>{subject} PDF</a>"
                            else:
                                response = f"PDF link not found for {subject} ({dept_name} {sem})"
                            return response

    if not response:
        response = 'Sorry, I don\'t have the PDF link for that. Try asking for a specific department, semester, and subject.'

    return response

if __name__ == '__main__':
    app.run(debug=True,host="192.168.0.112",port=5000)
