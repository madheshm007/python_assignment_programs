def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }

    cart["items"].append(item)

def update_price(price_tuple, new_price):
    try:
        price_tuple[1] = new_price

    except TypeError as e:
        print("\nTuple Error:", e)
        print("Tuples are immutable, so their elements cannot be changed.")

def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    
    discount_amount = total * (cart["discount"] / 100)
    final_total = total - discount_amount

    return final_total


cart1 = create_cart("Akash", discount=10)
cart2 = create_cart("Arun", discount=5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 800, 2)

add_to_cart(cart2, "Keyboard", 1500, 1)
add_to_cart(cart2, "USB Cable", 300, 3)

print("Customer 1 Cart:")
print(cart1)

print("\nCustomer 2 Cart:")
print(cart2)

print("\nTotal for", cart1["owner"], "=", calculate_total(cart1))
print("Total for", cart2["owner"], "=", calculate_total(cart2))

price_data = ("Laptop", 50000)

update_price(price_data, 45000)