import requests
data = requests.get('https://www.w3schools.com/html/default.asp')



print(data.text)

