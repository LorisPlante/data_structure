def out_of_stock_products(products):
    return sorted((id, product['price']) for id, product in products.items() if product['quantity'] == 0)