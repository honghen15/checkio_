import sendgrid
import json
import datetime

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def how_spammed(str_date):
    end_time = datetime.datetime.strptime(str_date, '%Y-%m-%d')
    start_time = end_time + datetime.timedelta(days=1)
    response = sg.client.suppression.spam_reports.get(query_params={
        'end_time': int(end_time.timestamp()),
        'start_time': int(start_time.timestamp())
    })

    print(end_time)
    print(start_time)

    print(json.loads(response.body))
    return len(json.loads(response.body))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')
