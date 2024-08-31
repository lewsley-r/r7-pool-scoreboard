from pyairtable import Api
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

api = Api(os.getenv('AIRTABLE_API_KEY'))
table = api.table('app5VgB4Gt5plSkne', 'r7-pool')
winners_table = api.table('app5VgB4Gt5plSkne', 'r7-pool-winners')

@app.route("/", methods=["GET", "POST"])
def display_scores():
    if request.method == "GET":
        winners = winners_table.all()
        records = table.all()
        sorted_records = []
        total = {'Glenn': 0, 'Ronan': 0}
        winner_records = []
        for winner in winners:
            temp_record = {}             
            temp_record['Name'] = winner['fields']['Name']
            temp_record['Month'] = winner['fields']['Month']
            winner_records.append(temp_record)
        for record in records:
            total['Glenn'] += record["fields"]["Glenn"]
            total['Ronan'] += record["fields"]["Ronan"]
            record["fields"]["id"] = record["id"]
            sorted_records.append(record["fields"])
        return render_template('new_scores.html', scores=sorted_records, total=total)
    table.create(
        {"Ronan": int(request.form["Ronan"]), "Glenn": int(request.form["Glenn"])})
    return redirect(url_for('display_scores'))


@app.route("/delete/<id>", methods=["POST"])
def delete_score(id):
    table.delete(id)
    return redirect(url_for('display_scores'))


if __name__ == '__main__':
    app.run(debug=True)
