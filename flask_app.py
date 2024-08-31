from pyairtable import Api
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

api = Api(os.getenv('AIRTABLE_API_KEY'))
table = api.table('app5VgB4Gt5plSkne', 'r7-pool')


@app.route("/", methods=["GET", "POST"])
def display_scores():
    if request.method == "GET":
        records = table.all()
        sorted_records = []
        total = {'Glenn': 0, 'Ronan': 0}
        for record in records:
            total['Glenn'] += record["fields"]["Glenn"]
            total['Ronan'] += record["fields"]["Ronan"]
            record["fields"]["id"] = record["id"]
            sorted_records.append(record["fields"])
        return render_template('new_scores.html', scores=sorted_records, total=total)
        # return render_template('new_scores.html')
    table.create(
        {"Ronan": int(request.form["Ronan"]), "Glenn": int(request.form["Glenn"])})
    return redirect(url_for('display_scores'))


@app.route("/delete/<id>", methods=["POST"])
def delete_score(id):
    table.delete(id)
    return redirect(url_for('display_scores'))


if __name__ == '__main__':
    app.run(debug=True)
