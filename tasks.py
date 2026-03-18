def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime(lst):
    return [num for num in lst if is_prime(num)]


def find_greatest_number(lst):
    if not lst:
        return None
    
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num