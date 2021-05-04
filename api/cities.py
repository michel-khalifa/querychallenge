from flask import jsonify
import sqlite3


def suggestions(q):
    # Create an empty list for our results
    results = []
    # Connect to the cities DB
    conn = sqlite3.connect('../db/cities.db')
    cur = conn.cursor()
    cities = cur.execute("SELECT name FROM cities where name like '" + '%' + q + '%' + "';").fetchall()
    # Loop through the data and add it to results list.
    for city in cities:
        results.append(city[0])
    # Use the jsonify function from Flask to convert the list of JSON format
    return jsonify(results)

