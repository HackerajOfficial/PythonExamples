
import random
ans=["0","1","3"]
Answer = random.randint(1,999)
ans[0]=Answer
op1=random.randint(1,999)
ans[1]=op1
op2=random.randint(1,999)
ans[2]=op2

ans.sort()

print("============Options================")
print("1. "+ str(ans[0]))
print("2. "+ str(ans[1]))
print("3. "+ str(ans[2]))


Guess = int(input("Guess:"))

if Guess == Answer:
    print("Congratulations!!!")
else:
    print("Sorry Ans:" +str(Answer))
