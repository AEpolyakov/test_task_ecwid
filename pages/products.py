
class Product:
    """model of product from search page"""
    def __init__(self, name: str, price: str, label_sale='', label_out_of_stock=''):
        self.name = name
        self.price = float(price.replace('$', ''))
        self.label_sale = label_sale
        self.label_out_of_stock = label_out_of_stock


class Products:
    """class that realises check product methods"""
    def __init__(self):
        self.products = []

    def append(self, name, price, label_sale='', label_out_of_stock=''):
        """append Product element to product list"""
        product = Product(name, price, label_sale, label_out_of_stock)
        self.products.append(product)

    def are_discount_only(self):
        """check that every product is with discount label"""
        for product in self.products:
            if not product.label_sale:
                return False
        return True

    def are_not_out_of_stock(self):
        """check that every product is not out of stock"""
        for product in self.products:
            if product.label_out_of_stock:
                return False
        return True

    def are_in_price_from(self, price_from):
        """check that every product price is more than given number"""
        for products in self.products:
            if price_from and (products.price < price_from):
                return False
        return True

    def are_in_price_to(self, price_to):
        """check that every product price is less than given number"""
        for products in self.products:
            if price_to and (products.price > price_to):
                return False
        return True

    def are_in_name_filter(self, filter_value: str):
        """check that every product name contains given string"""
        for products in self.products:
            if filter_value not in products.name:
                return False
        return True

    def __str__(self):
        result = ['\nPRODUCTS ARE:\n']
        for product in self.products:
            result.append(f'{product.name} {product.price} {product.label_sale} {product.label_out_of_stock}\n')
        return ''.join(result)
