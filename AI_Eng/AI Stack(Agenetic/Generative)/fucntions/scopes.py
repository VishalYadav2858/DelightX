# Scopes and name resolution

# ---- loca-inside a funciton
# ---- enclosing from outer funtiion if nested
# ---- gloal top levl script
# ---- Built in



# local,nonlocal,global

chai_type ="Plain"

def front_desk():
    def kitchchen():
        
        chai_type = "Irani"
        print(f"{chai_type}")
    kitchchen()
    # print(f"{chai_type}")
    
front_desk()

print(f"{chai_type}")




def specialchai_(*ingredients, **kargs):
    print(f"ingredients {ingredients}")
    print(f"kargs {kargs}")
    
specialchai_("Chai", "masala", name="papaiya")





