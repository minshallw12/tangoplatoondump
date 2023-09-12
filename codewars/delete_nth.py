def delete_nth(order,max_e):
    
    # create a dict counter for numbers
    # count occurences of each number up to the max
        #if count is less than the value in the counter dict
            # add it to the new list
    # return new list
    print(order)
    print(max_e)

    dict_counter = {}
    my_list = []
    
    if max_e == 0:
        return []
    
    for i in range(len(order)):
        #print(order[i])
        if order[i] not in dict_counter:
            dict_counter[order[i]] = 1
            my_list.append(order[i])
        else:
            if dict_counter[order[i]] < max_e:
                dict_counter[order[i]] += 1
                my_list.append(order[i])
   # print(dict_counter)
    return my_list



print(delete_nth([1,2,3,4,5], 1)) # [1,2,3,4,5]
print(delete_nth([1,2,4,2,5], 1)) # [1,2,4,5]
print(delete_nth([1,2,3,4,2,2,5], 2)) # [1,2,3,4,2,5]