chai = {"masal": "ginger", "quantity": 3,"type": "solid"}
# chai.keys
print(chai)
chaiii = dict(masala= "ginger", quantity= 3,type= "solid")
# print(chaiii.keys)
# print(chaiii.values)

chaha = {}
chaha["type"] = "strong"
chaha["sugar"] = "less"
print(chaha["type"])
del chaha["sugar"]
print(chaha)

print(f"is sugar in {'sugar' in chaha}")


customer_note = chaiii.get("masala", "NO NOTE")
print(f"{customer_note}")