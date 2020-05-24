def find_upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return s[i]
    return "No uppercase found"

def find_upper_rec(s,idx=0):
    if s[idx].isupper():
        return s[idx]
    if idx==len(s)-1:
        return "No upper case found"
    return find_upper_rec(s,idx+1)

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"


print(find_upper(input_str_1))
print(find_upper(input_str_2))
print(find_upper(input_str_3))

print(find_upper_rec(input_str_1))
print(find_upper_rec(input_str_2))
print(find_upper_rec(input_str_3))
