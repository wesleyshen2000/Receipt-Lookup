#Pull the data from the receipt and organize it by item: quantity
import requests
import json
    
from FileManager import FileManager
from src.Constants.FileLocationConstants import FolderLocationConstants
from src.Util.ConfigUtil import ConfigUtil

class Data:
    def __init__(self):
        self.fm = FileManager()
        self.tmp_path = FolderLocationConstants().get_temp_folder()

    def read_config_file(self):
        param = {}
        with open('../../config/config.txt') as f:
            for line in f:
                if line[0] != '#':
                    key,val = ConfigUtil.getValue(line)
                    param[key] = val
        return param

    def create_request(self):
        """
        Creates an initial request to gather data
        :return: All the items bought from Walmart
        :rtype: dict
        """
        data = self.read_config_file()

        #Check if tmp folder is created, if not create folder
        try:
            self.fm.create_folder(self.tmp_path)
        except FileExistsError:
            print("TMP Folder already exists")

        #Walmart Request
        #TODO: Error handling for bad response
        url = 'https://www.walmart.com/chcwebapp/api/receipts'
        response = requests.post(url,data=data).text
        response_dict = json.loads(response)
        print(response_dict)
        items = response_dict['receipts'][0]['items'] #Finds the items category
        results = {}
        for item in items:
            if item['upc'] in results:
                results[item['upc']]['quantity']+= 1
            else:
                #Adds new item into dictionary
                results[item['upc']] = {}
                results[item['upc']]['description']= item['description']
                results[item['upc']]['price'] = item['price']
                results[item['upc']]['quantity']= item['quantity']

                #Download image
                try:
                    #results[item['upc']]['imageUrl'] = item['imageUrl']
                    self.download_image(item['imageUrl'],self.tmp_path+item['description']+".png")
                except:
                    results[item['upc']]['imageUrl'] = None

    def download_image(self,url,path):
        if not self.fm.file_exist(path):
            file = open(path,'wb')
            response = requests.get(url)
            file.write(response.content)
        else:
            print("{} already exists".format(path))
test = Data()
test.create_request()