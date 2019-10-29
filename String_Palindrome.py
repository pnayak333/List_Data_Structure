my_str = "sexyysyyxes"
l = len(my_str)-1
print(l)
flag = False
for i in range(len(my_str)-1):
    if my_str[i] == my_str[l]:
        l = l-1
        flag = True
        if i >= l:
            break
    else:
        flag = False
        break
if flag == True:
    print("Palin")
else:
    print("Not")