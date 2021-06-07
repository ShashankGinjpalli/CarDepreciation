import requests

response = requests.get('http://localhost:3000/carListings/getSpecificListing?make=Honda&title=Accord&year=2017&zipcode=95123')
print(response.content)
