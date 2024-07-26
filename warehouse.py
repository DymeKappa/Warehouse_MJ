import sys

class Warehouse():

    def __init__(self, products_list):
        self.product_list = products_list

    def show_avaliable_products(self):
        print('Avaliable products:')
        for product in self.product_list:
            print(product)

    def add_product(self):
        self.product_name = input('Set product name: >>> ')
        if self.product_name not in self.product_list:
            self.product_list.append(self.product_name)
            print(f'Product {self.product_name} have been added to the Warehouse.')
        else:
            print('This product is already in stock.')

    def delete_product(self):
        self.product_name = input('Which product do you want to delete? >>> ')

        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            print(f'{self.product_name} have been deleted.')
        else:
            print("There isn't such a product.")


shop_warehouse = Warehouse(['Milk', 'Water', 'Egg'])

while True:
    print("Choose '1' to display stocks.")
    print("Choose '2' to add product.")
    print("Chppse '3' to delete product.")
    print("Choose '4' to exit.")
    user_choose = int(input('>>> '))
    if user_choose == 1:
        shop_warehouse.show_avaliable_products()
    elif user_choose == 2:
        shop_warehouse.add_product()
    elif user_choose == 3:
        shop_warehouse.delete_product()
    elif user_choose == 4:
        sys.exit()
    else:
        print("!--Choose correct option.")