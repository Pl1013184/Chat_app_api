#test
import requests
message=input("Enter your message: ")
response = requests.post('http://127.0.0.1:5000/main/chat',data={'data':message})
print(response.text)
x=requests.get('http://127.0.0.1:5000/main/chat')
print(x.text)