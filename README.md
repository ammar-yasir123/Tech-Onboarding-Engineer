# Tech-Onboarding-Engineer

This is a script to upload a profile picture for a user based on their user ID.

How it works:
- Imports a CSV file into a dataframe
- Stores all user IDs found in the dataframe into a list
- Searches for images with valid image formats with file names corresponding to user ID
- Sends a PUT request to create new profile picture field/update profile picture field of user
- Uploads profile picture for user

Libraries used:
- requests
- pandas
- os
- imghdr
