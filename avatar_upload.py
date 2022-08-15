# -*- coding: utf-8 -*-
"""
@author: Ammar Yasir

Comment: This code is based on the assumption that script is stored in, 
and runs in the same folder as the CSV file and profile pictures.
"""


import requests
import pandas as pd
import os.path
import imghdr

#Check current working directory
ROOT_DIR = os.getcwd()

#Name of CSV file. Can be changed upon customer's request
CSV_FILENAME = 'user_list.csv'

#Path for CSV file 
CSV_FILEPATH = os.path.join(ROOT_DIR, CSV_FILENAME)

#Define valid image formats
IMAGE_FORMATS = ('bmp', 'BMP', 'jpeg', 'JPEG', 'png', 'PNG', 'tiff', 'TIFF')

#API URL
url = "https://de.staffbase.com/api/users/"

#Authorization token
auth = {"content-type": "application/json", "Authorization": "<auth-key>" }

#Read csv file and store in Dataframe
df = pd.read_csv(CSV_FILEPATH)

#Store UserIDs in list
userid_list = df['externalID'].tolist()


#Loop to check profile pictures for all users in CSV file
for user in userid_list:
    
    
    #API URL for specific user
    url_id = url+"{}".format(user)
    

    #Check if user profile picture exists using 'externalID' and list of valid formats
    for i in IMAGE_FORMATS:
        #Check if file is valid image
        try:
            pic_format = imghdr.what('{}.{}'.format(user, i))
        
            #Store name of file in variable
            pic_name = '{}.{}'.format(user, i)
#            print(pic_name)
    
    
            #Create header using userID and providing avatar image in folder
            data = {"userID":user,"avatar":pic_name}
                    
            #Send PUT request to create new field called 'avatar' and upload profile picture
            r = requests.put(url, data=data, headers=auth)
            
            #Change value of PUT URL for next entry
            url_id = url
            
        #Continue if image with specific format doesn't exist
        except Exception as e:
                
        #Uncomment to print exception error
#            print (e)
            continue
    
