name = ["vishal", "yash", "pratham", "randi"]
bills = [30,5,678,456,321]

for nam,amount in zip(name,bills):
    print(f"{nam} paid {amount}")