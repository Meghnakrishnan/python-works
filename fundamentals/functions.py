# print(dir(list))
# print(dir(dict))
lst = [
      [1,34],
      [40,5],
      [5,70]
]

#print all number greater than 50
# for ls in lst:
#     for i in ls:
#         if i > 50:
#             print(i)
#using list comprehenssion
# numbers = [num for ls in lst for num in ls if num>50]
# print(numbers)
#largest number of list
# m = max(lst)
# print(m)
# print(max([n for ls in lst for n in ls]))
# print([n for ls in lst for n in ls if n == 5])
#find pair that contain max value
# m = max([n for ls in lst for n in ls])
# max_pair = [ls for ls in lst if m in ls]
# print(max_pair)
# ==== try=====binary search
# lst2 = [1,2,3,4]
# out = 7
