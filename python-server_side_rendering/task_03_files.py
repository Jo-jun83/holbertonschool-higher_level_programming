#!/usr/bin/python3
from flask import Flask, render_template, request
from json import load
import json, csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        items = load(f).get('items') or []
    return render_template('items.html', items=items)

@app.route('/products/')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    if source == "json":
        with open('products.json') as f:
            data = load(f)
            products = data
    elif source == "csv":
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            products = [row for row in reader]
    else:
        return render_template('product_display.html',
                               error_message="Wrong source")

    if product_id:
        filtered_products = [product for product in products if str(
            product['id']) == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                   error_message="Product not found")
        products = filtered_products
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)