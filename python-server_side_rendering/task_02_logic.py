#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items_list():
    """Route that reads items from JSON and renders the template"""
    try:
        # Lecture du fichier JSON
        with open('items.json', 'r') as f:
            data = json.load(f)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []

    # Envoi de la liste à ton template
    return render_template('items.html', items=items)


# Route par défaut optionnelle (utile pour tester)
@app.route('/')
def home():
    return "<h1>Welcome to the Items App</h1><p>Go to <a href='/items'>/items</a></p>"


if __name__ == '__main__':
    app.run(debug=True)
