'''
Name: Group 9 Alex Haban Addyson Stansel
email: habanaj@mail.uc.edu, ENTER EMAIL HERE
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




