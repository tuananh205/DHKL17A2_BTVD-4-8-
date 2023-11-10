a=int(input("nhập a:"))
b=int(input("nhập b:"))

ucln = a if a < b else b
while True:
    if a % ucln == 0:
        break 
    ucln = 1
    bcnn = (a*b)//ucln
    print(f"bội chung nhỏ nhất của {a} và {b} là:{bcnn}")