from django.conf import settings

from .models import Cart, CartItem

class CartManager:
    def __init__(self, request):
        """
            Initialize the cart. 
        """
        self.session = request.session
        cart_id = self.session.get(settings.CART_SESSION_ID)
        
        if cart_id:
            cart = Cart.objects.filter(id = cart_id).first()
        elif request.user.is_authenticated:
            # if there is no cart id but the user is auth then try to get the cart from user
            cart = Cart.objects.filter(user = request.user).first()
        
        # if user is anonymous or the auth user has no previous cart, then generate a new Cart
        if not cart:
            cart = Cart.objects.create()
        
        # make sure the cart id is correct
        self.session[settings.CART_SESSION_ID] = str(cart.id)
        self.cart = cart
        self.save()
    
    def add(self, product, quantity=1, override_quantity=False): 
        """
            Add a product to the cart or update its quantity. 
        """
        cart_item = self.cart.items.filter(product = product).first()
        if not cart_item:
            cart_item = CartItem.objects.create(cart = self.cart, product = product, price = product.price, quantity = quantity)
        else:
            if override_quantity:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
    
    def save(self):
        self.session.modified = True

    def remove(self, product): 
        """
            Remove a product from the cart. 
        """
        cart_item = self.cart.items.filter(product = product).first()
        if cart_item:
            cart_item.delete()
    
    def __len__(self): 
        """
            Count all items in the cart. 
        """
        return len(self.cart.items)

    def clear(self): 
        self.cart.items.all().delete()

    