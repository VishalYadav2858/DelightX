# staff = [("amit": 45),("vishal":12), ("yash": 56)]
staff = [("vishal",23),("yash",12),("pradeep",56)]

for name,age in staff:
    if age>18:
        print(f"{name} u r eligible")
    else:
        print(f"{name} u r not")
