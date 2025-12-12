# def process_order(item, quantity):
#     try:
#         price = {"masala": 20}[item]
#         cost = price * quantity
#         print(f"Total cost is {cost}")
#     except KeyError:
#         print("Item not found in menu")
#     except TypeError:
#         print("Quantity must be a number")

# process_order("ginger", 2)
# process_order("masala", "two")

# raise ur own error
# def brew_masala(flavour):
#     if flavour not in ["masala", "papaya", "elaichi"]:
#         raise ValueError ("Unsupported chai")
#     print(f"brewing {flavour} chai")
    
# brew_masala("m")










#  creating custom exception
class OutofIngrediantsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutofIngrediantsError("Missing chai or milk")
    print("Chai is ready...")

make_chai(0,1)







class OutofIngrediantsError(Exception):
    pass

def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 10}
    if flavour not in menu:
        raise OutofIngrediantsError("that chai is not available")
    if not isinstance(cups, int):
        raise TypeError("Number of cups must be an integer")
    total = menu[flavour] * cups
    print(f"your total is {total}")

try:
    bill("masala", 2)
except Exception as e:
    print("Error:", e)
finally:
    print("Thanks for visit")
    
    
    
    
    
    
    
    







op