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
print(f'Add product id=1 and id=2 to cart')
product_ids = [1, 2]

headers = {'Authorization': f'Token {token}'}

for id in product_ids:
    pload = {"cart": cart['id'], "product": id,"quantity": 3}
    response = requests.post(f"http://127.0.0.1:8000/cartitems/", data=pload, headers=headers)

    if response.status_code < 400:
        print(f'Product {id} added to cart')
        print(response.json())
        
    else:
        print(f'ERROR Product {id} NOT added to cart')
        print(response.json())
        

print('-'*20)
print(f'Remove all products from cart')

headers = {'Authorization': f'Token {token}'}

for item in cart['items']:
    response = requests.delete(f"http://127.0.0.1:8000/cartitems/{item['id']}", headers=headers)

    if response.status_code == 204:
        print('Cart_item deleted')
    else:
        print('Cart_item NOT deleted')
        print(response.json())

