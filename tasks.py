def find_second_max(lst):
    if len(lst) < 2:
        return None
    first = float('-inf')
    second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    
    if second == float('-inf'):
        return None
    return second