import requests
from requests import request
import numpy as np
import json
from datetime import datetime
import csv
import pandas as pd
from IPython.display import display, HTML


start_time = datetime.now()
# 1. AUTHENTICATION (Get OAuth2 Token)
auth_url = "https://api.xbrl.us/oauth2/token"
auth_data = {
    "grant_type": "password",
    "client_id": "__________________", #Replace with your actual client secret
    "client_secret": "_________________________",  # Replace with your actual client secret
    "username": "_______________________",           # Replace with your username/email from XBRL website
    "password": "__________________",           # Replace with your password from XBRL website
    "platform": "pc"
}

auth_response = request("POST", auth_url, data=auth_data)
print(auth_response.text) #This will print your ACCESS TOKEN access_token which you should insert when making a GET request, the Bearer works for 1 hour
end_time = datetime.now()
print(f"✅ API call completed at: {end_time.strftime('%H:%M:%S')}")
print(f"⏱️ Execution duration: {end_time - start_time}") 

access_token = "________________________" #replace with Bearer

endpoint = 'document'
# TEMP removed 
#text_search = ['21.1'] # , 'subsidiary' , 'subsidiaries'
fields = ['document-type',
          'document.uri',
          'dts.id.sort(DESC)',
          'document.example' ,
          'document.limit(10)',
          'report.id'
          ]

rows_to_display = 10 # Set as 10 to display 10 rows in the notebook
unique = True
params = {
    'document.text-search': '21.1',
    #','.join(text_search),
    'fields': ','.join(fields)
    #'report.id' : '226471'
    
    
}

#api_url = f"https://api.xbrl.us/api/v1/fact/search?report.id=226471&fields=entity.name,dimensions.count,dimensions,entity.cik,period.fiscal-period,period.end,period.instant,period.year,concept.local-name.sort(ASC),fact.numerical-value,fact.value,report.source-id,footnote.text,footnote.role"
api_url = 'https://api.xbrl.us/api/v1/' + endpoint + '/search'
#if unique:
#    api_url += "?unique"
orig_fields = params['fields']
offset_value = 0
res_df = []
count = 0
query_start = datetime.now()
printed = False
run_query = True


headers = {
    "Authorization" : f"Bearer {access_token}",
    "Content-type" : "application/json; charset=utf-8"
}

#x = 10
# + f'?limit={x}'
data_response = request("GET", api_url, headers=headers, params=params)
print(data_response.text)
print(data_response.status_code)  # Should be 200
print(data_response.text)  # Might show HTML error page or plain text error

myjson = data_response.json()

myjson

res_df = myjson['data']

df = pd.DataFrame(res_df)
#pd.options.display.float_format = '{:,.2f}'.format
# display(HTML(df.to_html(max_rows=rows_to_display)))