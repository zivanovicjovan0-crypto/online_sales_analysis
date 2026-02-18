def remove_product(self, product_name):
    for product in self.products:
        if product.name == product_name:
            self.products.remove(product)
            print(f"{product_name} uklonjen.")
            return
    print("Proizvod nije pronađen.")
