from flask import Flask, redirect, render_template, request, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE = "users.csv"

#Read users from the CSV file
def read_users():
    if not os.path.exists(CSV_FILE):
        return []
    
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)
    
#Add User to the CSV File
def add_user(name, email):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email])

#Home Route
@app.route('/')
def home():
    users = read_users()
    return render_template('home.html', users=users)

#About
@app.route('/about')
def about():
    return render_template('about.html')

#Register New User
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('home'))
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)