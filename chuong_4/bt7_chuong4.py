def calculate_sum_of_digits(N):
    sum_of_digits = 0
    
    # Chuyển đổi số nguyên N thành chuỗi để thao tác với từng chữ số
    digits = str(N)
    
    # Lặp qua từng chữ số trong chuỗi
    for digit in digits:
        # Chuyển đổi chữ số từ kiểu string sang kiểu int và cộng vào sum_of_digits
        sum_of_digits += int(digit)
    
    # Trả về tổng các chữ số
    return sum_of_digits
