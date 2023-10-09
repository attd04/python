import requests
from datetime import datetime

today = datetime.now()

# making account
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "autumntd"
TOKEN = "qwertyuiop"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)

# making a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Step Tracker",
    "unit": "steps",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# posting pixel

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '19444',
}

#response3 = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)

# updating pixels
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230917"

new_pixel = {
    "quantity": "3497"
}

# response4 = requests.put(url=update_endpoint, json=new_pixel, headers=headers)


# deleting pixels
response5 = requests.delete(url=update_endpoint, headers=headers)
