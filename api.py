

import requests


# url ="https://randomuser.me/api/"

url ="https://api.coinbase.com/v2/prices/ETH-USD/buy"

response = requests.get(url)
data=response.json()

# print("The name is :" ,data["results"][0]["name"]["first"],data["results"][0]["name"]["last"])

# print("The mail-id is: ",data["results"][0]['email'])

# print("The employee-id is:",data["results"][0]["location"]["street"]["number"])

# print("The location of the employee is:",data["results"][0]["location"]["street"]["name"])

# print("The address of the employee is: ",data["results"][0]["location"]["city"],data["results"][0]["location"]["state"],data["results"][0]["location"]["country"],data["results"][0]["location"]["postcode"])

# print("The phone no is: ",data["results"][0]["phone"])

print ("The amount is :" ,data['data'] ["amount"])
 
      
      