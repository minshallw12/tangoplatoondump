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

