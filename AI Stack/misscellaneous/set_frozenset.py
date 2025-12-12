essential = {"Hello", "yess", "cool"}
required = {"ok", "cool", "wassup"}

final = essential | required
final2 = essential & required
is_present = {f"is 'ok' present in {'ok' in required}"}
print(is_present)

print(final)
print(final2)

only_essential = essential - required
print(only_essential)