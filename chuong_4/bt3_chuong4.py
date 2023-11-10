m = int(input("Nhập m: "))
n = int(input("Nhập n (m < n): "))
if m < n and m > 0:
    i = m
    while i <= n:
        if i % m == 0:
            print(i)
        i += 1  
        i = i + 1 
        print(i)
