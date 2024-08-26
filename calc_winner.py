from pyairtable import Api
import os
from datetime import datetime

api = Api(os.getenv('AIRTABLE_API_KEY'))
api2 = Api(os.getenv('AIRTABLE_API_KEY'))
winners_table = api.table('app5VgB4Gt5plSkne', 'r7-pool-winners')
score_table = api2.table('app5VgB4Gt5plSkne', 'r7-pool')


def calcuate_winner():
    score_records = score_table.all()
    total = {'Glenn': 0, 'Ronan': 0}
    for record in score_records:
        total['Glenn'] += record["fields"]["Glenn"]
        total['Ronan'] += record["fields"]["Ronan"]
        record["fields"]["id"] = record["id"]
    current_month = datetime.now().strftime('%h')  # Feb
    current_day = datetime.now().strftime('%d')  # 23
    if int(current_day) == 26:
        winners_table.create(
            {"Name": max(total, key=total.get),  "Month": current_month})
        for record in score_records:
            score_table.delete(record['id'])
    else:
        print('Nothing to do here!')


if __name__ == '__main__':
    calcuate_winner()
