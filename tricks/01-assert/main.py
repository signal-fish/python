def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'] #just for debug
    return price

shoes = {
            'name': 'Fancy Shoes',
            'price': 14900,
        }
print(apply_discount(shoes, 0.25))
# apply_discount(shoes, -0.25)
