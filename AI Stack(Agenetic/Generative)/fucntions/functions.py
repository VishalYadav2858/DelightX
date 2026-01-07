def price(amount, VAT):
    return amount * (100+VAT)/100

orders = [ 30,45,89]

for amount in orders :
    final_amount = price(amount, 10)
    print(f"og{amount}, final:{final_amount}")

