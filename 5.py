def change_char(str1):

    char=str1[0]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]

    return str1


word=input("Enter any word")
print("Before replacement: ",word)
print("After replacement: ",change_char(word))

    




