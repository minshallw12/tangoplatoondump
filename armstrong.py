# def is_character_match(string1, string2):
#     count1={}
#     count2={}
#     for l1 in string1:
#         if l1 not in count1:
#             count1[l1]=1
#         else:
#             count1[l1]+=1
#     for l2 in string2:
#         if l2 not in count2:
#             count2[l2]=1
#         else:
#             count2[l2]+=1
#     return count1==count2
    

# def anagrams_for(word, list_of_words):
#     result=[]
#     for item in list_of_words:
#         if is_character_match(word,item):
#             result.append(item)
#     return result

# print(anagrams_for('target', ['artget']))

def sum_pairs(list,sum):
    result=[]
    for i in range(len(list)):
        for j in range(i):
            if list[i]+list[j]==sum:
                result.append([list[i], list[j]])
    return result

print(sum_pairs([1,2,3,4,5], 9)) # [[4,5]]
print(sum_pairs([1,2,3,4,5], 7)) # [[2,5], [3,4]]
print(sum_pairs([3, 1, 5, 8, 2], 27))

print(range(0,2,1))