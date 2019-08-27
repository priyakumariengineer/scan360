#Name : CMC_Twitter_Fetch.py
#Description : 
#To pull out twitter handle of all the currency and make a xls file. This uses APIs provided by CMC.
#This twitter handles will be used for monitoring using twitter APIs in other module.
#
#Production key CMC :
#ce263360-1f12-462b-8c15-842a2823df04
#
#Test key CMC:
#fe440872-5552-4791-ba1d-6c241ce9c931
#
#production link: https://pro-api.coinmarketcap.com
#Test link: https://sandbox-api.coinmarketcap.com/
#
#Documentation : https://coinmarketcap.com/api/documentation/v1/
#Pro usage Tracking : https://pro.coinmarketcap.com/account
#Sandbox Tracking : https://sandbox.coinmarketcap.com/account
#
#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import math
import openpyxl 

#sandbox
url_map = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/map'
url_info = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/info'

#production
#url_map  = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
#url_info = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

parameters_map = {
}

parameters_info_ids = {
  'id': '1,2'
}

headers = {
  'Accepts': 'application/json',
  #TEST
  'X-CMC_PRO_API_KEY': 'fe440872-5552-4791-ba1d-6c241ce9c931',
  #PRO
  #'X-CMC_PRO_API_KEY': 'ce263360-1f12-462b-8c15-842a2823df04',
}


Map_details_list = [  'Dummy',
                      'Main_id' , 
                      'Name', 
					  'Symbol', 
					  'URL_name', 
					  'Is_Active', 
					  'status',
                      'first_historical_data', 
				      'last_historical_data', 
				      'platform', 
				      'platform_name', 
				      'platform_token_address' , 
				      'catagory_coin_tocken', 
				      'logo_url',
					  'description',
					  'date_added',
					  'notice',
					  'tags_minable_or_not',
					  'website',
                      'technical_doc',
                      'explorer',
                      'source_code',
                      'message_board',
                      'chat',
                      'announcement',
                      'reddit',
                      'twitter'
				   ]

session = Session()
session.headers.update(headers)

#creating an excel file for writing data.
wb = openpyxl.Workbook()
sheet = wb.active 
sheet.title = "CMC_details"

# writing titles in excel file
# carefull about index
for i in range(1, len(Map_details_list)):
  c1 = sheet.cell(row = 1, column = i)
  c1.value = Map_details_list[i]  

#fetching list of availible currency and ids.

try:
  response = session.get(url_map, params=parameters_map)
  data_map = json.loads(response.text)
  data_map_list = data_map['data']
  length_map = len(data_map_list)
  id_list = []
  
  for i in range(length_map): 
    id_list.append(data_map_list[i]['id'])
	
    sheet.cell(row = i+2, column = Map_details_list.index('Main_id')).value = data_map_list[i]['id']
    sheet.cell(row = i+2, column = Map_details_list.index('Name')).value = data_map_list[i]['name']
    sheet.cell(row = i+2, column = Map_details_list.index('Symbol')).value = data_map_list[i]['symbol']
    sheet.cell(row = i+2, column = Map_details_list.index('URL_name')).value = data_map_list[i]['slug']
    sheet.cell(row = i+2, column = Map_details_list.index('Is_Active')).value = data_map_list[i]['is_active']
    sheet.cell(row = i+2, column = Map_details_list.index('status')).value = "NA"
    sheet.cell(row = i+2, column = Map_details_list.index('first_historical_data')).value = \
    data_map_list[i]['first_historical_data']
    sheet.cell(row = i+2, column = Map_details_list.index('last_historical_data')).value = \
    data_map_list[i]['last_historical_data']
	
    if data_map_list[i]['platform']:
      curr_platform_dict = data_map_list[i]['platform']
      
      sheet.cell(row = i+2, column = Map_details_list.index('platform')).value = "YES"
      sheet.cell(row = i+2, column = Map_details_list.index('platform_name')).value = \
      curr_platform_dict['name']
      sheet.cell(row = i+2, column = Map_details_list.index('platform_token_address')).value = \
      curr_platform_dict['token_address']
      
    else:
    
      sheet.cell(row = i+2, column = Map_details_list.index('platform')).value = "NA"
      
	
  #print(id_list)
  #print(data['data'][1]['id'])
  #print(data['data'])
  
  
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print("There is some issue fetching ID map , here is the error !!! " )
  print(e)
  
#fetching list of twitter accounts

# length_id = len(id_list)

# for i in range(0, length_id, 100 ):

  # Curr_id_list = list(id_list[i: i+100 if i+100 < length_id else length_id ])
  # parameters_info_ids['id'] = ','.join(map(str, Curr_id_list)) 

  # try:
    # response = session.get(url_info, params=parameters_info_ids)
    # data_info = json.loads(response.text)
    # data_info = str(data_info).encode('utf8')
    # print(data_info)
    # print("************************************************************")
    # print("************************************************************")
  # except (ConnectionError, Timeout, TooManyRedirects) as e:
    # print("There is some issue fetching meta data of currency , here is the error !!! " )
    # print(e)
	
wb.save("CMC_Coin_Details_Auto.xlsx") 
	