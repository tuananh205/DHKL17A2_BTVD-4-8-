#giải hệ phương trình bậc nhất
def solve_linear_equation(A, B, C):
    D = A - B
    
    if D == 0:
        if A == 0:
            print("Hệ phương trình vô số nghiệm")
        else:
            print("Hệ phương trình vô nghiệm")
    else:
        x = C / D
        y = -A / B
        print(f"Nghiệm của hệ phương trình: x = {x}, y = {y}")

#tính toán số ngày của một tháng một năm nào đó
def calculate_days_in_month(year):
    is_leap = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    print("Năm nhuận") if is_leap else print("Không phải năm nhuận")
    days = 31
    print(f"Số ngày của tháng 1: {days}")

#thuật toán tìm ước số chung lớn nhất
def find_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    print(f"Ước số chung lớn nhất: {a}")