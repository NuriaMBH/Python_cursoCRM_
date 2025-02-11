import requests
url='https://jsonplaceholder.typicode.com/posts'
url='https://dummyjson.com/todos'
url='https://jsonplaceholder.typicode.com/photos'
response=requests.get(url)
print(response.json())