def str_function(s):
    
    a=len(s)
    if('ing'==s[a-3:a+1]):
        return s+'ly'
    else:
        return s+'ing'


s=input("Enter a string")
print(str_function(s))
