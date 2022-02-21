# DS LIFO

# create empy stack
# loop the brackets
# if close brackets in dict pop the last element else append
# if stack Failure 

par = "[{()}](){}{}[][][][]()()}"

par_dict = {"}": "{", "]":"[", ")": "("}

stack= []

for i in par:
    if i in par_dict and len(stack):
        if stack[-1] == par_dict[i]:
            stack.pop()
    else:
        stack.append(i)
print(stack)
if stack:
    print("Failure")
else:
    print("pass")
