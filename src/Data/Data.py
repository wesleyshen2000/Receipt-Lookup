#Pull the data from the receipt and organize it by item: quantity
import requests
import json
def read_file():
    """
    Reads the config file to get parameter information
    :return: list of parameters for request
    :rtype: dict
    """
    param = {}
    with open('../../config/config.txt') as f:
        for line in f:
            if line[0] != '#':
                line = line.replace(':','')
                line = line.rstrip('\n')
                result = line.split(' ')
                param[result[0]] = result[1]

    return param

def create_request():
    """
    Creates an initial request to gather data
    :return: All the items bought from Walmart
    :rtype: dict
    """
    data = read_file()

    url = 'https://www.walmart.com/chcwebapp/api/receipts'
    response = requests.post(url,data=data).text
    response_dict =  json.loads(response)
    items = response_dict['receipts'][0]['items'] #Finds the items category
    results = {}
    for item in items:
        if item['upc'] in results:
            results[item['upc']]['quantity']+= 1
        else:
            results[item['upc']] = {}
            results[item['upc']]['description']= item['description']
            results[item['upc']]['price'] = item['price']
            results[item['upc']]['quantity']= item['quantity']
    print(results)
    print(type(results['007874223747']['quantity']))

create_request()