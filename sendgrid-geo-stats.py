import sendgrid

API_KEY = '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'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def best_country(str_date):
    # params = {'end_date': '2016-04-01', 'country': 'US', 'aggregated_by': 'day', 'limit': 1, 'offset': 1,
    #           'start_date': '2016-01-01'}
    # response = sg.client.geo.stats.get(query_params=params)
    # return str(response.body)
    # data = [{
    #     'date': '2016-01-01',
    #     'stats': [
    #         {
    #             'type': 'country',
    #             'name': 'AT',
    #             'metrics': {'clicks': 1, 'opens': 1, 'unique_clicks': 1, 'unique_opens': 1}
    #         },
    #         {
    #             'type': 'country',
    #             'name': 'AU',
    #             'metrics': {'clicks': 0, 'opens': 31, 'unique_clicks': 0, 'unique_opens': 22}
    #         }
    #     ]
    # }]
    # response = sg.client.geo.stats.get(query_params={
    #     'start_date': str_date,
    #     'end_date': str_date
    # })
    #
    # max_data = max(data[0]['stats'], key=lambda a: a['metrics']['unique_clicks'])
    # return max_data['name']
    response = sg.client.geo.stats.get(query_params={
        'start_date': str_date,
        'end_date': str_date,
    })
    import json
    print('======', end='')
    print(json.loads(response.body), end='')
    print('======')
    data= json.loads(response.body)
    maxdata = data[0]['stats'][0]['metrics']['opens']
    country_open = data[0]['stats'][0]['name']
    for i in data[0]['stats']:
        if i['metrics']['opens'] > maxdata:
            maxdata = i['metrics']['opens']
            country_open = i['name']
    return country_open

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Your best country in 2016-01-01 was ' + best_country('2016-01-01'))
    print('Check your results')
