from flask import Flask, request, jsonify, render_template # type: ignore
from pymongo import MongoClient # type: ignore
from urllib.parse import quote_plus
import logging
logging.basicConfig(level=logging.DEBUG)
import pdb


import os

app = Flask(__name__)

# MongoDB setup

# username = quote_plus('ayush270236')
# password = quote_plus('Sachin')

client = MongoClient(f"mongodb+srv://ayush270236:Ayush123@flight.0hfe1ls.mongodb.net/?retryWrites=true&w=majority&appName=flight")
db = client["flight"]
collection_flights = db.flight
collection_notifications = db.notifications


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_flight', methods=['GET'])
def get_flight():
    try:
        flight_id = request.args.get('flight_id')
        flight = db.flight.find_one({"flight_id": flight_id})
        if flight:
            flight['_id'] = str(flight['_id'])  # Convert ObjectId to string
            return jsonify(flight)
        else:
            return jsonify({"error": "Flight not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500    


if __name__ == '__main__':
    app.run(debug=True)
