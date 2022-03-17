import requests

KEY = "" # your upload.systems key

def upload(file_location):

    FILE = open(file_location, "rb")
    
    data = {
        "key": KEY
    }
    
    files = {
        "file": FILE
    }
    
    response = requests.post("https://api.upload.systems/images/upload", data=data, files=files)
        
    if response.json()["error"]:
        raise Exception(response.json()["displayMessage"])
        
    return response.json()["url"]


""" Example """
print(upload("FILE LOCATON"))
