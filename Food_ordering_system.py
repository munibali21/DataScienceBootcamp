class FoodOrderingSystem:
    def __init__(self, user_name, order, quantity, payment):
        self.user_name = user_name
        self.order = order
        self.quantity = quantity
        self.payment = payment
        self.inventory = {'biryani': 150, 'khaosaw': 200, 'noodles': 40, 'roti': 30, 'butter': 20,
                          'shawarma': 250, 'chicken rolls': 260, 'nihari': 500, 'paye': 500, 'handi': 600, 'karhai': 1000}
        self.total_order = []

    def place_order(self):
        if self.order in self.inventory:
            order_details = {'food': self.order, 'quantity': self.quantity}
            self.total_order.append(order_details)
            print('How much quantity do you want?')
            print(f'You want {self.quantity} plates of {self.order}')
            print('What is the mode of payment? COD/Credit card/E wallet? :')
        else:
            print("It's not in our menu")

    def calculate_bill(self):
        total_cost = 0
        for order in self.total_order:
            food_item = order['food']
            quantity = order['quantity']
            if food_item in self.inventory:
                total_cost += self.inventory[food_item] * quantity
        return total_cost

# Example usage:
name = input('Enter name: ')

asim = FoodOrderingSystem(name, None, None, None)

while True:
    food_name = input("Enter food (type 'quit' to stop): ")

    if food_name.lower() == 'quit':
        break

    qty = int(input(f'Enter quantity for {food_name}: '))

    asim.order = food_name
    asim.quantity = qty
payment = input('Enter payment mode: ')
if payment.lower()=='credit'or 'E Vallet' or 'COD':
  print('selected')
else:
  print('''we don't have this payment method ''')

asim.payment = payment
asim.place_order()
total_bill = asim.calculate_bill()
print(f'Total Bill Amount: {total_bill}')
