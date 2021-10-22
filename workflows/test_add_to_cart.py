import requests

print('-'*20)
print('Login as superuser')
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
product_id = 2
print(f'Get product {product_id}')

response = requests.get(f'http://127.0.0.1:8000/products/{product_id}/')

if response.status_code == 200:
    print('Product found')
    print(response.json())
else:
    print('Product NOT found')
    print(response.text)

print('-'*20)
print(f'Get user cart')

response = requests.get(f"http://127.0.0.1:8000/carts/?user={user_data['pk']}", headers=headers)

if response.status_code == 200:
    print('Cart found')
    data = response.json()
    cart = data['results'][0]
    print(cart)
else:
    print('Cart NOT found')
    print(response.text)

print('-'*20)
print(f'Add product {product_id} to cart')


pload = {"cart": cart['id'], "product": product_id,"quantity": 3}
headers = {'Authorization': f'Token {token}'}
response = requests.post(f"http://127.0.0.1:8000/cartitems/", data=pload, headers=headers)

if response.status_code < 400:
    print('Product added to cart')
    print(response.json())
    print(response.status_code)
else:
    print('ERROR Product NOT added to cart')
    print(response.json())
    print(response.status_code)