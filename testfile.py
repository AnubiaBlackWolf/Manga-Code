import matplotlib.pyplot as plt
import numpy as np


my_mangaList = []
not_mymangaList = []
#Creating a Tuple
mangaTuple = ("jojo","Kaiju No.8","Choujin X" )

y = np.my_manga([25, 25, 25, 25])
plt.pie(y)
plt.legend()
plt.show()


#Append allows the ability to add elements to the list
my_mangaList.append('Bleach')
my_mangaList.append('Chainsaw Man')
my_mangaList.append('Naruto')
my_mangaList.append('Black Clover')

#Appended second list
my_mangaList.append("Hunter X Hunter")
my_mangaList.append("One Piece")
my_mangaList.append("Berserk")

#Combining the two list together
my_mangaList.extend(not_mymangaList)
print(not_mymangaList)

#Adding the list to the tuple
not_mymangaList.extend(mangaTuple)
print(not_mymangaList)

#Identfies the index where the new element will take place of
i = my_mangaList.index('Black Clover')

#Will insert the new element in the index specified index
my_mangaList.insert(2, 'D.Gray-Man')

#unpacking a list by assigning values to variables
#b, c, n, bc, d = my_mangaList

x = "FML"
k = "Fist"
age = 36
txt = "My name is jimmy and I am {}"

def myfunc():
    global k # creates a global variable that takes precedent over all variables with same name
    k = "Tiger Man"
    print("Python is " + x)
    print(my_mangaList[0] + " is trash ")
    print(" i hit people with my " + k)
    print(txt.format(age))
    print()

myfunc()
print(my_mangaList[2:7])

#print(b)
#print(c)
#print(n)
#print(bc)
#print(d)
print(len(my_mangaList))

print(my_mangaList)
print(txt.format(age))
print()





