def format_duration(seconds): 
    if seconds == 0:
        return "now"
    
    time_dict = {                                       
        "year": 1*365*24*60*60,
        "day": 1*24*60*60,
        "hour": 1*60*60,
        "minute": 1*60,
        "second": 1
    }
    
    singles = [time for time in time_dict.keys()]       
    plurals = [time + 's' for time in time_dict.keys()]

    def remove_that_damn_comma(lst):
        if lst == []:
            return []
        sanitized_lst = []
        for chars in lst[len(lst)-1]:
            if chars != ",":
                sanitized_lst.append(chars)
        sanitized = ''.join(sanitized_lst)
        lst.pop()
        lst.append(sanitized)
        return ' '.join(lst)
    
    def get_change(amount, time_value, appender):           
        count = 0                                           
        while amount >= time_value:                         
            count += 1                                      
            amount -= time_value                            
        appender.append(count)
        return amount                                       
    
    count_each_time = []
    temp_amount = seconds                     
    for value in time_dict.values():                    
        temp_amount = get_change(temp_amount, value, count_each_time)

    final_times = []                                       
    for i in range(len(count_each_time)):                        
        number = count_each_time[i]
        if number > 1:
            if i == len(count_each_time)-1:
                final_times.append(str(number) + ' ' + plurals[i])
            else:
                final_times.append(str(number) + ' ' + plurals[i] + ',')
        elif number == 1:
            if i == len(count_each_time)-1: # is it the -1
                final_times.append(str(number) + ' ' + singles[i])
            else:
                final_times.append(str(number) + ' ' + singles[i] + ',')

    remove_comma = list(final_times.pop())                 
    if remove_comma[len(remove_comma)-1] == ',':
        remove_comma.pop()
    last_item = ''.join(remove_comma)   
    refactored = remove_that_damn_comma(final_times)
    
    num_of_denoms = 0                                        
    for num in count_each_time:
        if num != 0:
            num_of_denoms += 1 

    if num_of_denoms == 1:                                   
        return f"{last_item}"
    else:
        return f"{refactored} and {last_item}"