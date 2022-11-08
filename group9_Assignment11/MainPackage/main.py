'''
Name: Group 9 Alex Haban Addyson Stansel
email: habanaj@mail.uc.edu, ENTER EMAIL HERE
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This demonstrates that we can run a json to access an API server and create a dictionary from it. 
Citations: https://catalog.data.gov/dataset?q=hospital&sort=views_recent+desc&res_format=CSV&ext_location=&ext_bbox=&ext_prev_extent=-150.46875%2C-80.17871349622823%2C151.875%2C80.17871349622823
           Link to the CSV file I used. It's the 2009 VHA Facility...
Anything else that's relevant:
'''
import json # Built-in, no pip install required
import requests # Add with pip
#https://www.ers.usda.gov/developer/data-apis/arms-data-api/
response = requests.get('https://api.ers.usda.gov/data/arms/state?api_key=W2pq7tbvlExznt92jH1jekdBoqX3yRsRdJOwNR2M')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
print(parsed_json)   




