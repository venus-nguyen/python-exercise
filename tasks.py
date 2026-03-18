def find_greatest_number(lst):
    if not lst:
        return None
    
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
