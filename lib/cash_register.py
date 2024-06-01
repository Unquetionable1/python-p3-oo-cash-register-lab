class CashRegister:
  def __init__(self,discount=0):
    self.discount=discount
    self.total=0
    self.items=[]
    self.prev_total=[]
  def add_item(self,title,price,quantity=1):
    self.total+=price*quantity
    self.prev_total.append(
            {"item": title, "quantity": quantity, "price": price}
        )
    for _ in range(quantity):
      self.items.append(title)
    
    
  def apply_discount(self):
    if self.discount:
      self.total =float( self.total * ((100-self.discount )/ 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
       print("There is no discount to apply.")
  def void_last_transaction(self):
    if not self.prev_total:
        return "There are no transactions to void."
    
    last_transaction = self.prev_total.pop()
    self.total -= last_transaction["price"] * last_transaction["quantity"]
    
    for _ in range(last_transaction["quantity"]):
        self.items.pop()
    
