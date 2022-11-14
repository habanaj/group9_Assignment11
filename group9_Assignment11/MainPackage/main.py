'''
Name: Group 9 Alex Haban Addyson Stansel
email: habanaj@mail.uc.edu, stansean@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This demonstrates that we can run a json to access an API server and create a dictionary from it. 
Citations: https://www.ers.usda.gov/developer/data-apis/arms-data-api/
           Link that we used for the API
Anything else that's relevant:
'''
# Import packages to access API
import json 
import requests 
# Create variable for API content
response = requests.get('https://api.ers.usda.gov/data/arms/state?api_key=W2pq7tbvlExznt92jH1jekdBoqX3yRsRdJOwNR2M')
json_string = response.content

# Convert all content to string format    
parsed_json = json.loads(json_string) # Now we have a python dictionary
print(parsed_json)   

id = {'id 1': 'OO',
      'id 2': '05',
      'id 3': '06',
      'id 4': '12',
      'id 5': '13',
      'id 6': '17',
      'id 7': '18',
      'id 8': '19',
      'id 9': '20',
      'id 10': '27',
      'id 11': '29',
      'id 12': '31',
      'id 13': '37',
      'id 14': '48',
      'id 15': '53',
      'id 16': '55'}

state_names = {'name 1': 'All survey states',
               'name 2': 'Arkansas',
               'name 3': 'California',
               'name 4': 'Florida',
               'name 5': 'Georgia',
               'name 6': 'Illinois',
               'name 7': 'Indiana',
               'name 8': 'Iowa',
               'name 9': 'Kansas',
               'name 10': 'Minnesota',
               'name 11': 'Missouri',
               'name 12': 'Nebraska',
               'name 13': 'North Carolina',
               'name 14': 'Texas',
               'name 15': 'Washington',
               'name 16': 'Wisconsin'
    
    }
for key,value in state_names.items():
    print(key, ' : ', value)
    
for key,value in id.items():
    print(key, ' : ', value)
