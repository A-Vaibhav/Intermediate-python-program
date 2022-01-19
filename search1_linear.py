def linear_search(element,list1):
    list2 = list1.copy()
    list2.sort()
    flag = 0

    for i in list2:
        if i == element:
            flag+=1
            break

        
    if flag == 1:
        return f"Element {i} found"
    else:
        return f"Element {element} not in the List"

data = [10,5,2,6,3,1]
result = linear_search(100,data)
print(result)