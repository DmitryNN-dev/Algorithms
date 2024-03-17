# V1

needle = "qwer"
haystack = "sdf qwer"

# index = -1
# for i in range(len(haystack)-len(needle)+1):
#     success = True
#     for j in range(len(needle)):
#         if needle[j] != haystack[i+j]:
#             success = False
#             break
#     if success:
#         index = 1
#         break

# print(index)

# V2:

for i in range(len(haystack) - len(needle) + 1):
    success = True 
    for j in range(len(needle)): 
        if needle[j] != haystack[i + j]: 
            success = False 
            break 
    if success: 
        index = i 
        break 
else:
    index = -1

print(index)