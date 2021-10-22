import requests

['login', 'add_product_to_cart', 'add_product_to_cart', 'checkout']

class Workflow:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.actions = []
        self.token = ''

    def set_actions(self, actions):
        self.actions = actions
    
    def run(self):
        for action in self.actions:
            action()

    def generate_headers(self, token):
        headers = {'Authorization': f'Token {token}'}
        return headers

    # ---- ACTIONS ------------------
    def login(self):
        pload = {'username':'superuser','password':'testing'}
        if self.verbose:
            print('-'*20)
            print('Login as superuser')
        
        response = requests.post('http://127.0.0.1:8000/rest-auth/login/', data=pload)

        if 'key' in response.json():
            token = response.json()['key']
            if self.verbose:
                print('Login successful')
                print('token = ', token)
        else:
            print('EXCEPTION IN ACTION: LOGIN')
            raise Exception(response.text)

        self.token = token

    def add_product_to_cart(self):
        headers = self.generate_headers(self.token)
        cart = self.get_cart()
        id = 1
        pload = {"cart": cart['id'], "product": id,"quantity": 3}
        if self.verbose:
            print('-'*20)
            print(f"Add product {pload['product']} to cart")
        
        response = requests.post(f"http://127.0.0.1:8000/cartitems/", data=pload, headers=headers)

        if response.status_code < 400:
            cart_item = response.json()
            if self.verbose:
                print('Product added to cart')
                print(response.json())
        else:
            print('EXCEPTION IN ACTION: ADD PRODUCT TO CART')
            raise Exception(response.text)
        
        return cart_item
        
        
    def get_user_profile(self):
        headers = self.generate_headers(self.token)
        if self.verbose:
            print('Get user profile')
    
        response = requests.get('http://127.0.0.1:8000/rest-auth/user/', headers= headers)

        if response.status_code < 400:
            user = response.json()
            if self.verbose:
                print('User profile')
                print(user)
        else:
            print('EXCEPTION IN ACTION: GET USER PROFILE')
            raise Exception(response.text)
        
        return user


    def get_product(self):
        product_id = 1
        if self.verbose:
            print(f'Get product {product_id}')

        response = requests.get(f'http://127.0.0.1:8000/products/{product_id}/')

        if response.status_code == 200:
            product = response.json()
            if self.verbose:
                print('Product found')
                print(product)
        else:
            print('EXCEPTION IN ACTION: GET PRODUCT')
            raise Exception(response.text)
        
        return product

    def get_cart(self):
        headers = self.generate_headers(self.token)
        user = self.get_user_profile()
        if self.verbose:
            print('-'*20)
            print(f'Get user cart')

        response = requests.get(f"http://127.0.0.1:8000/carts/?user={user['pk']}", headers=headers)

        if response.status_code == 200:
            data = response.json()
            cart = data['results'][0]
            if self.verbose:
                print('Cart found')
                print(cart)
        else:
            print('EXCEPTION IN ACTION: GET CART')
            raise Exception(response.text)
        
        return cart



    def clean_cart(self):
        headers = self.generate_headers(self.token)
        cart = self.get_cart()
        if self.verbose:
            print('-'*20)   
            print(f'Remove all products from cart')

        for item in cart['items']:
            response = requests.delete(f"http://127.0.0.1:8000/cartitems/{item['id']}", headers=headers)

            if response.status_code == 204:
                if self.verbose:
                    print('Cart_item deleted')
            else:
                print('EXCEPTION IN ACTION: CLEAN CART')
                raise Exception('cart_item not deleted')
