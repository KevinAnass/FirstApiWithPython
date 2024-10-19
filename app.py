from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

from config import Config

# Initialize the Flask app
app = Flask(__name__, template_folder="tempates")
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)


@app.route("/")
def index():
    # Execute a raw SQL query to get all users
    result = db.session.execute(
        "SELECT [CategoryID],[CategoryName],[Description],[CreatedAt],[UpdatedAt] FROM [dbo].[Categories]"
    ).fetchall()
    users = [{"id": row[0], "name": row[1], "email": row[2]} for row in result]
    return render_template("index.html", users=users)


# Define an API endpoint to get all users
@app.route("/api/getCategories", methods=["GET"])
def get_users():
    # Execute a raw SQL query to get all users
    result = db.session.execute(
        text("SELECT CategoryID,CategoryName,Description FROM Categories")
    ).fetchall()
    categories = [
        {"CategoryID": row[0], "CategoryName": row[1], "Description": row[2]}
        for row in result
    ]
    return jsonify(categories)


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
