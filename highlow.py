#import sys
#sys.path.append('/home/vishalli/ml/codes/game_data')
from game_data import data
import random
score=0
flag=True
while(flag):
    while(True):
        a1=random.choice(data);
        a2=random.choice(data);
        f1=a1['follower_count']
        f2=a2['follower_count']
        if(f1>f2):
            ans='A'
        else:
            ans='B'
        print(f"Compare A:{a1['name']},a {a1['description']}, from {a1['country']}.")
        print("____VS____")
        print(f"AgainstB:{a2['name']},a {a2['description']}, from {a2['country']}.")
        choice=input("enter who has more followers?Type 'A' or 'B")
        if(choice==ans):
            score=score+1;
            print(f"You Won and score: {score}")

        else:
            print(f"You Loss and score: {score}")
            break

    ct=input("Want to continue type y or n")
    if(ct=="y"):
       continue
    else:
        flag=False
   


