str_1=input("Enter the first string: ")
str_2=input("Enter the second string: ")
str_1=str_1.lower()
str_2=str_2.lower()
if  (len(str_1)==len(str_2)):
	sorted_str_1=sorted(str_1)
	sorted_str_2=sorted(str_2)
	if sorted_str_1==sorted_str_2:
		print("Given strings are anagrams")
	else:
		print("Given strings are not anagrams")
else:
	print("Given strings are not anagrams")
