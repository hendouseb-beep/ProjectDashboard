from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Charger les projets depuis projects.json
def load_projects():
    try:
        with open('projects.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Sauvegarder les projets dans projects.json
def save_projects(projects):
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=4, ensure_ascii=False)

projects = load_projects()

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

# Nouvelle route pour gérer le formulaire
@app.route('/add', methods=['POST'])
def add_project():
    name = request.form['name']
    status = request.form['status']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    owner = request.form['owner']

    new_project = {
        "name": name,
        "status": status,
        "start_date": start_date,
        "end_date": end_date,
        "owner": owner
    }

    projects.append(new_project)
    save_projects(projects)

    return redirect(url_for('index'))
