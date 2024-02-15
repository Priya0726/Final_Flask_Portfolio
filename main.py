from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to establish connection with SQLite database
def get_db_connection():
    conn = sqlite3.connect('journal.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint to create a new journal entry
@app.route('/entries', methods=['POST'])
def create_entry():
    # Existing code for creating a journal entry
    pass

# Endpoint to retrieve all journal entries
@app.route('/entries', methods=['GET'])
def get_entries():
    # Existing code for retrieving journal entries
    pass

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define the index route
@app.route('/')
def index():
    return render_template('index.html')

# Your existing routes and functions

# Run the application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8087")
