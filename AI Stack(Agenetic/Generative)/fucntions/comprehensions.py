# # list comprehensions
# menu = [
#     "masala iced",
#     "ginger",
#     "garlic iced",
#     "something"
# ]
# 
# iced_tea= [tea for tea in menu if "masala" in tea]
# print(iced_tea)

 





recepie = {
    "masala" : ["guinger" , "water", "kalimirch"],
    "lemon" : ["lemon" , "water", "kalimirch"],
    "normal" : ["adrak" , "water", "kalimirch"]
 }

unique = {spice for ingredients in recepie.values() for spice in ingredients}
print(unique)







# tea_prices_inr = {
#     "masala" : 34213,
#     "ginger" : 365,
#     "lemon" : 3765
# }
# 
# usd = { tea:price/90 for tea,price in tea_prices_inr.items()}
# print(usd)







