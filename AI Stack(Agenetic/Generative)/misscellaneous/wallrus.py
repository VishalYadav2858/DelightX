# value =13
# ramainder = value % 5
# 
# if ramainder:
#     print(f"Remainder is not zero {ramainder}")
    
    
    


# value =13
# 
# if (remainder := value %5):
#     print(f"Remainder is not zero. It is {remainder}")
# 
# 
# available_sizes = ["small", "medium", "large"]
# 
# if (requested_chai:= input("Enter cup size: ")):
#     print(f"Serving {requested_chai} chai!!")
# else:
#     print(f"{requested_chai} size not available")
#     
    
    
    
    
    
    
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 75, "coupon": "P50"},
    {"id": 3, "total": 30, "coupon": "P10"},
]

discouts = {
    "P20" : (0.2, 0),
    "P50" : (0.5, 0),
    "P10" : (0, 10)
}

for user in users:
    percent, fixed = discouts.get(user["coupon"], (0,0))
    discounted = user["total"]* percent + fixed
    print(f'{user["id"]} paid {user["total"]} and got discount of rupees {discounted}')
    
    
    
    
    
    
    
   