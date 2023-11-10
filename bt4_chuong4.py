a=float(input("nhập a: "))
b=float(input("nhập b: "))
c=float(input("nhập c: "))
max_value = a if a>b else b
max_value = max_value if max_value>c else c
print(f"số lớn nhất là:{max_value}")