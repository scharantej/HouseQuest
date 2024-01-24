
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database Connection
connection = sqlite3.connect('house_listing.db')
cursor = connection.cursor()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# House Search Page
@app.route('/house_search', methods=['GET', 'POST'])
def house_search():
    if request.method == 'POST':
        # Get search criteria
        location = request.form['location']
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        num_bedrooms = request.form['num_bedrooms']
        num_bathrooms = request.form['num_bathrooms']

        # Query the database for matching properties
        properties = cursor.execute('''
            SELECT * FROM properties
            WHERE location=? AND price BETWEEN ? AND ?
            AND num_bedrooms=? AND num_bathrooms=?
        ''', (location, min_price, max_price, num_bedrooms, num_bathrooms)).fetchall()

        # Redirect to the house list page with the search results
        return redirect(url_for('house_list', properties=properties))

    return render_template('house_search.html')


# House List Page
@app.route('/house_list')
def house_list():
    # Get the search results from the previous page
    properties = request.args.get('properties')

    # Convert the string of properties to a list
    properties = eval(properties)

    return render_template('house_list.html', properties=properties)


# House Details Page
@app.route('/house_details/<property_id>')
def house_details(property_id):
    # Get the details of the specified property from the database
    property_details = cursor.execute('''
        SELECT * FROM properties
        WHERE property_id=?
    ''', (property_id,)).fetchone()

    return render_template('house_details.html', property_details=property_details)


# Mortgage Calculator Page
@app.route('/mortgage_calculator')
def mortgage_calculator():
    return render_template('mortgage_calculator.html')


# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the contact information from the form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send the contact information to the real estate agent
        # (This could be done using an email API or other method)

        # Redirect to the home page with a confirmation message
        return redirect(url_for('home', message="Your message has been sent."))

    return render_template('contact.html')


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
