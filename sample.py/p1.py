class Restaurant:
    def __init__(self, name):
        self.name = name
        self.bills = []
    
    def add_bill(self, bill):
        self.bills.append(bill)
    
    def get_total_revenue(self):
        return sum(bill.total_amount for bill in self.bills)


class Bill:
    def __init__(self, bill_id, customer_name):
        self.bill_id = bill_id
        self.customer_name = customer_name
        self.items = []
        self.tax_rate = 0.1
    
    def add_item(self, item_name, price, quantity=1):
        self.items.append({
            'name': item_name,
            'price': price,
            'quantity': quantity
        })
    
    def calculate_subtotal(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate
    
    @property
    def total_amount(self):
        return self.calculate_subtotal() + self.calculate_tax()
    
    def display_bill(self):
        print(f"\n{'='*40}")
        print(f"Bill ID: {self.bill_id} | Customer: {self.customer_name}")
        print(f"{'='*40}")
        for item in self.items:
            print(f"{item['name']:<20} ${item['price']:.2f} x {item['quantity']} = ${item['price']*item['quantity']:.2f}")
        print(f"{'-'*40}")
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Tax (10%): ${self.calculate_tax():.2f}")
        print(f"Total: ${self.total_amount:.2f}")
        print(f"{'='*40}\n")


# Example usage
if __name__ == "__main__":
    restaurant = Restaurant("Pizza Palace")
    
    bill1 = Bill(1, "John Doe")
    bill1.add_item("Margherita Pizza", 12.99, 2)
    bill1.add_item("Garlic Bread", 4.99, 1)
    bill1.add_item("Coke", 2.99, 2)
    
    bill1.display_bill()
    restaurant.add_bill(bill1)
    
    bill2 = Bill(2, "Jane Smith")
    bill2.add_item("Pasta Carbonara", 13.99, 1)
    bill2.add_item("Tiramisu", 5.99, 2)
    
    bill2.display_bill()
    restaurant.add_bill(bill2)
    
    print(f"Total Revenue: ${restaurant.get_total_revenue():.2f}")