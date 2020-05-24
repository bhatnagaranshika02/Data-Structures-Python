vowels="aeiou"
def conscount(s):
    consonant=0
    for i in range(len(s)):
        if s[i] not in vowels and s[i].isalpha():
            cononant+=1
        return consonant

def recursive(s):
    if s=='':
        return 0
    if s[0].lower() not in vowels and s[0].isalpha():
        return 1+ recursive(s[1:])
    else:
        return recursive(s[1:])


input_str = "abc de"
print(input_str)
print(conscount(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(recursive(input_str))
