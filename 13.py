from collections import Counter

def charfreq(s):

	d = Counter(s)
	for i in d:
		print(i+str(d[i]), end=" ")


word=input("Enter any string")
print("Character frequency of given word ",word," is : ")
charfreq(word)



