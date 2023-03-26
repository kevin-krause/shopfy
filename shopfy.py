from shopify import Shopify

shop_url = '...'
api_key = '...'
password = '...'
session = Shopify(shop_url, api_key, password)

products = session.Product.find()
for product in products:
    print(product.title)
