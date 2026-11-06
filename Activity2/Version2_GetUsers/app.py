from flask import Flask, jsonify
from database import create_db_table, get_users, insert_user, user as sample_user

app = Flask(__name__)


def initialize_users():
    create_db_table()
    if not get_users():
        insert_user(sample_user)


@app.get("/get_users")
@app.get("/api/get_users")
def api_get_user_names():
    return jsonify([record["name"] for record in get_users()])


if __name__ == "__main__":
    initialize_users()
    app.run(host="0.0.0.0", port=3000)
