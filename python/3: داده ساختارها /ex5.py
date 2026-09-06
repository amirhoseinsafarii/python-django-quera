def calc(lst: list) -> tuple:
    lst = sorted(lst)
    
    average = sum(lst) / len(lst)
    
    if len(lst) % 2 == 1:
        median = lst[len(lst) // 2]
    else:
        median = (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    
    maximum = lst[-1]
    
    return average, median, maximum