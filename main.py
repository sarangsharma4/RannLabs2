import requests

# api-endpoint
URL = "http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement"


# defining a params dict for the parameters to be sent to the API
PARAMS = {
    "Gender":"All",
    "MacAddress":"b8:27:eb:45:c7:21",
    "Location":"",
    "Business":"",
    "Age":""
}


# sending get request and saving the response as response object
r = requests.post(url=URL, params=PARAMS)

# extracting data in json format
#data = r.json()

data_test={"ID":101, "VideoUrl":"https://www.youtube.com/watch?v=KHMTn9Az92w"}

video_name=str(data_test["ID"])
video_link=str(data_test["VideoUrl"])

# printing the output
print("The video name is: %s" %video_name, "The video link is: %s" %video_link)
