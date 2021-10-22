import requests

print('-'*20)
print('Test login')
pload = {'username':'superuser','password':'testing'}
response = requests.post('http://127.0.0.1:8000/rest-auth/login/', data=pload)

if 'key' in response.json():
    token = response.json()['key']
    print('Login successful')
    print('token = ', token)
else:
    print('Login failed')
    print(response)
    print(response.text)

print('-'*20)
print('Test registration')
pload = {
    "username": "testuser1",
    "email": "testuser1@example.com",
    "password1": "testing123#",
    "password2": "testing123#"
}
response = requests.post('http://127.0.0.1:8000/rest-auth/registration/', data=pload)

if 'key' in response.json():
    token = response.json()['key']
    print('Registration successful')
    print('token = ', token)
else:
    print('Registration failed')
    print(response)
    print(response.text)

print('Get user profile')
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/rest-auth/user/', headers= headers)

if response.status_code < 400:
    user_data = response.json()
    print('User profile')
    print(user_data)
else:
    print('failed user profile')
    print(response)
    print(response.text)


