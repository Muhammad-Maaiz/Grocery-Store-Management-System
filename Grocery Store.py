# GROCERY STORE:
class Grocery_Store:
    print("***WELCOME TO GROCERY STORE***".center(100))
    print("------------------------------".center(100))
    def __init__(self):
        self.admin_products = {
            "Lays":  {"Price": 15, "Quantity": 100, "Company_name": "Lays", "Selling_Price": 20},
            "Pepsi": {"Price": 70, "Quantity": 100, "Company_name": "Pepsico International", "Selling_Price": 80},
            "Sooper": {"Price": 15, "Quantity": 100, "Company_name": "Peak Freans", "Selling_Price": 20},
            "Milk": {"Price":70, "Quantity":100, "Company_name":"ABC","Selling_price":80}
    }
        self.customer_products = {
            "Lays": {"Price": 20, "Quantity": 100, "Company_name": "Lays"},
            "Pepsi": {"Price": 70, "Quantity": 100, "Company_name": "Pepsico International"},
            "Sooper": {"Price": 20, "Quantity":100, "Companay_name": "Peak Freans"},
            "Milk": {"Price": 70, "Quantity":100, "Company_name":"ABC"}

        }

    def customer_show_all_products(self):
        if not self.customer_products:
            print("No items available.")
        else:
            print("\nAvailable Products:\n")
            for product, details in self.customer_products.items():
                print(f"{product}:  {details['Price']} Rs")

    def view_products(self, products):
        if not self.admin_products:
            print("\nProducts Not Avalible")
        else:
            print("\nAvailable Products:")
            for product, details in products.items():
                print(f"{product}: Price - {details['Price']}, Quantity - {details['Quantity']}, Company - {details['Company_name']}")
    
    def add_product(self, products):
        product_name = input("Enter Product name: ")
        price = int(input("Enter Price: "))
        quantity = int(input("Enter quantity: "))
        company_name = input("Enter Company name: ")
        selling_price = float(input("Enter Selling Price: "))
        products[product_name.capitalize()] = {"Price": price, "Quantity": quantity, "Company_name": company_name, "Selling_Price": selling_price}
        print(f"{product_name.capitalize()} added to the inventory.")

    def update_product(self, products):
        product_name = input("Enter product name to update: ")
        if product_name.capitalize() in products:
            print("What do you want to update?")
            print("1. Price")
            print("2. Quantity")
            print("3. Company Name")
            print("4. Selling Price") 

            update_choice = int(input("Enter your choice: "))

            if update_choice == 1:
                new_price = int(input("Enter new price: "))
                products[product_name.capitalize()]["Price"] = new_price
                print(f"{product_name.capitalize()} price updated.")
            elif update_choice == 2:
                new_quantity = int(input("Enter new quantity: "))
                products[product_name.capitalize()]["Quantity"] = new_quantity
                print(f"{product_name.capitalize()} quantity updated.")
            elif update_choice == 3:
                new_company_name = input("Enter new company name: ")
                products[product_name.capitalize()]["Company_name"] = new_company_name
                print(f"{product_name.capitalize()} company name updated.")
            elif update_choice == 4:
                new_selling_price = float(input("Enter new selling price: "))
                products[product_name.capitalize()]["Selling_Price"] = new_selling_price
                print(f"{product_name.capitalize()} selling price updated.")
            else:
                print("Invalid choice.")
        else:
            print("Product not found.")

    def remove_product(self, products):
        product_name = input("Enter product name to remove: ")
        if product_name.capitalize() in products:
            del products[product_name.capitalize()]
            print(f"{product_name.capitalize()} removed from the inventory.")
        else:
            print("Product not found.")

    def generate_bill(self, selected_items):
        total_bill = 0
        print("\n---------------------------------")
        print("Bill:")
        print(f"Name - {self.customer_name.capitalize()}")
        for item in selected_items:
            print(f"{item['item']}: Quantity - {item['quantity']}, Price - {item['price']}")
            total_bill += item['price']
        print("----------------------------------")
        print(f"Your Total Bill is: {total_bill}")
        print("----------------------------------")

    def get_feedback(self):
        self.feedback = input("Please provide your feedback: ")
        print("Thank you for your feedback!")

    def calculate_profit(self):
        profit = 0
        for self.product_name, product_details in self.admin_products.items():
            purchase_price = product_details.get("Price", 0)
            selling_price = product_details.get("Selling_Price", 0)
            quantity_sold = product_details.get("Quantity", 0)
            
            profit_per_item = (selling_price - purchase_price) * quantity_sold
            print(f"Profit in {self.product_name.capitalize()} is:{profit_per_item} Rs")
            profit += profit_per_item
        
        print(f"Your Total profit in all products is: {profit} Rs")
    
    def customer(self):
        self.customer_name = input("\nEnter your name: ")
        self.customer_show_all_products()
        selected_items = []
        while True:
            item_name = input("\nEnter the item name or 'exit' to finish: ")
            if item_name.capitalize() == 'Exit':
                break
            
            quantity = int(input("Enter the quantity: "))

            if item_name.capitalize() in self.customer_products:
                item_details = self.customer_products[item_name.capitalize()]
                available_quantity = item_details['Quantity']

                if quantity <= available_quantity:
                    price = item_details['Price']
                    total_price = price * quantity
                    selected_items.append({"item": item_name, "quantity": quantity, "price": total_price})
                else:
                    print(f"Only {available_quantity} quantity of {item_name.capitalize()} available.")
            else:
                print("Item not available")

        self.generate_bill(selected_items)

    def Admin(self):
        admin_password = input("Enter the Admin Password: ")
        if admin_password == "M@@IZ":
            while True:
                print("\nAdmin Options:\n")
                print("1. View Products")
                print("2. Add Products")
                print("3. Update Products")
                print("4. Remove Products")
                print("5. Calculate Profit")
                print("6. Exit")
                admin_choice = int(input("\nEnter your choice: "))

                if admin_choice == 1:
                    self.view_products(self.admin_products)
                elif admin_choice == 2:
                    self.add_product(self.admin_products)
                elif admin_choice == 3:
                    self.update_product(self.admin_products)
                elif admin_choice == 4:
                    self.remove_product(self.admin_products)
                elif admin_choice == 5:
                    self.calculate_profit()
                elif admin_choice == 6:
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Incorrect password. Please try again.")

    def display(self):
        while True:
            print("\nPlease select an option:\n")
            print("1. Customer")
            print("2. Admin")
            print("3. exit")
            user_choice = int(input("\nEnter your choice: "))

            if user_choice == 1:
                self.customer()
                my_grocery_store.get_feedback()
                break
            elif user_choice == 2:
                self.Admin()
            elif user_choice == 3:
                break
            else:
                print("Invalid choice.")

my_grocery_store = Grocery_Store()
my_grocery_store.display()