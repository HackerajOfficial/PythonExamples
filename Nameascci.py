'''import os
>>> a = ["home", "myusername", "Workdir", "notes.txt"]
>>> os.sep.join(a)'''

'''We are trying to make that type of program which takes names through key board and convert them into ascci value'''
import os
def ascciConverter(x):
     return ord(x)
   

word = 'raaz'
b=[]
for x in word:
    c = ascciConverter(x)
    b.append(c)
    if(len(word)==len(b)):
        for i in b:
            print(i)