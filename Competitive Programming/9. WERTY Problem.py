str=input("Enter your string: ")
#Define two lists containing the keys ; one standard and one right shift.
list1=['Q','W','E','R','T','Y','U','I','O','P','[',']','A','S','D','F','G','H','J','K','L',';','Z','X','C','V','B','N','M',',','.','/']
list2=['W','E','R','T','Y','U','I','O','P','[',']','A','S','D','F','G','H','J','K','L',';','Z','X','C','V','B','N','M',',','.','/']

#Loop begins
for i in str:
   ## If the character is a space, print it as space only
   if i==" ":
     print(" ",end="")
   else:
     #find index of list 1 and match it with index of list 2 and then print
     print(list1[list2.index(i)],end="")
