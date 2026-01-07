# chai  = "Ginger chai"
# 
# def preparing_chai(order):
#     print("preparing", order)
# 
# preparing_chai(order="Kola")
# print(chai) 


# 
# def chai_status(cups):
#     if cups ==0:
#         return  "Sorry no chai"
#     # print(cups)
#     return "serving ur chai"
#     
# print(chai_status(0))        
# print(chai_status(5))        
  
        
        
        
cha_types = ["kadak", "naram", "kadak", "green"]

strong_chai= list(filter(lambda chai: chai == "kadak", cha_types))

print(cha_types)