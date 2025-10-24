from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

# 🧩 Charger les projets depuis le fichier JSON
def load_projects():
    try:
        with open('projects.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 💾 Sauvegarder les projets
def save_projects(projects):
    with open('projects.json', 'w', encoding='utf-8') as f:
        json.dump(projects, f, indent=4, ensure_ascii=False)

# Charger les projets existants
projects = load_projects()

# 🏠 Route principale (affichage du dashboard)
@app.route('/')
def index():
    return render_template('index.html', projects=projects)

# ➕ Route pour ajouter un projet
@app.route('/add', methods=['POST'])
def add_project():
    client = request.form['owner']
    name = request.form['name']
    status = request.form['status']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    team = int(request.form['team'])
    progress = int(request.form['progress'])

    new_project = {
        "client": client,
        "name": name,
        "status": status,
        "start_date": start_date,
        "end_date": end_date,
        "team": team,
        "progress": progress
    }

    projects.append(new_project)
    save_projects(projects)
    return redirect(url_for('index'))

# ✏️ Route pour afficher le formulaire d’édition
@app.route('/edit/<int:index>', methods=['GET'])
def edit_project(index):
    project = projects[index]
    return render_template('edit.html', project=project, index=index)

# 💾 Route pour enregistrer la mise à jour
@app.route('/update/<int:index>', methods=['POST'])
def update_project(index):
    projects[index]['owner'] = request.form['owner']
    projects[index]['name'] = request.form['name']
    projects[index]['status'] = request.form['status']
    projects[index]['start_date'] = request.form['start_date']
    projects[index]['end_date'] = request.form['end_date']
    projects[index]['team'] = request.form['team']
    projects[index]['progress'] = request.form['progress']

    save_projects(projects)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_project(index):
    # Supprime le projet du tableau
    del projects[index]

    # Sauvegarde la nouvelle liste
    save_projects(projects)

    # Retour au tableau principal
    return redirect(url_for('index'))

# 🚀 Lancer le serveur Flask
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except OSError:
        app.run(host="0.0.0.0", port=8080, debug=True)
