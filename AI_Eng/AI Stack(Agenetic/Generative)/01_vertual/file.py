#  Index Error: 

# key error 
# zerodivision error
# type error
# name error

chai_menu = {"masala" : 30 , "ginger" : 40}

try: 
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are enterring is not present ")

print("Hi")











# // try,except,else and finally

def ser_chai(flavour):
    try:
        print(f"priparing {flavour} chai... ")
        if flavour == "unknown":
            raise ValueError("we don't know that flavour")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please")

ser_chai("masala")
ser_chai("unknown")        








# cathing multiple exception

def process_order(item,quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * item
    except KeyError:
        print(f"Total cois is {cost}")
        
    except TypeError:
        print("quantity must be in number")
        
process_order("masala", 2)
process_order("masala", 4)
    