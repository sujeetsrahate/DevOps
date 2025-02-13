import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)




# import requests #you can do lots of things like put list

# response=requests.get("https://www.google123.com")
# print(response.status_code)
# print(response)
# print(response.content)