from pyairtable import Api
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

api_key = os.getenv('AIRTABLE_API_KEY')
# api = Api(api_key)
table = api.table('app5VgB4Gt5plSkne', 'r7-pool')


@app.route("/", methods=["GET", "POST"])
def display_scores():
    if request.method == "GET":
        # return table.all()
        return api_key


@app.route("/delete/<int:id>", methods=["POST"])
def delete_score(id):
    return redirect(url_for('display_scores'))


if __name__ == '__main__':
    app.run(debug=True)
