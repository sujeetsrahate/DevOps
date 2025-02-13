import requests

# response= requests.post('https://httpbin.org/post', data={'key':'value'})
# response= requests.put('https://httpbin.org/put', data={'key':'value'}) 
# response= requests.delete('https://httpbin.org/delete', data={'key':'value'}) 
response= requests.get('https://httpbin.org/get', data={'key':'value'}) 
print(response.status_code)
print(response.content)