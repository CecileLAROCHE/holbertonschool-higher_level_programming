from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ------------------------------
# FONCTIONS POUR LECTURE DES FICHIERS
# ------------------------------
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })
    return products


# ------------------------------
# ROUTE PRINCIPALE
# ------------------------------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    try:
        if source == 'json':
            products = read_json()
        elif source == 'csv':
            products = read_csv()
        elif source == 'sql':
            products = read_sqlite()
        else:
            return render_template('product_display.html',
                                   error="Wrong source")
    except Exception as e:
        return render_template('product_display.html',
                               error=f"Error loading data: {e}")

    # Si un id est fourni → on filtre
    if product_id:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
