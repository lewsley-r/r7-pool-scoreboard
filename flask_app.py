from pyairtable import Api
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

api = Api(os.getenv('AIRTABLE_API_KEY'))
table = api.table('scores', 'r7-pool')


@app.route("/", methods=["GET", "POST"])
def display_scores():
    if request.method == "GET":
        return table.all()


@app.route("/delete/<int:id>", methods=["POST"])
def delete_score(id):
    return redirect(url_for('display_scores'))


if __name__ == '__main__':
    app.run(debug=True)
