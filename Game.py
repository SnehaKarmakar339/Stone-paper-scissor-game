import random
# print('''Enter any one out of the 3
# stone -> "st" 
# paper -> "pr" 
# scissors -> "sc" ''') 
def game():
  print('''**Enter any one out of the 3
stone -> "st" 
paper -> "pr" 
scissors -> "sc"** ''') 
  u=input("Enter your choice :")
  comp=random.randint(1,3)
 #comp=2
  ref={"st":1,"pr":2,"sc":3}
  user=ref[u]
  if(comp==1 and user==2):
    print("you win")
    return 1
  elif(comp==1 and user==3):
    print("you loose")
    return 0
  elif(comp==2 and user==1):
    print("you loose")
    return 0
  elif(comp==2 and user==3):
    print("you win")
    return 1
  elif(comp==3 and user==1):
    print("you win")
    return 1
  elif(comp==3 and user==2):
    print("you loose")
    return 0
  elif(comp==user):
    return -1
r="y"
while(r=="y"):
  us=0
  cs=0
  t=int(input("Enter the number of turns for each round (3 or 5 or 10) :"))
  for i in range (1,t+1):
    f=game()
    if(f==1):
      us+=1
    elif(f==0):
      cs+=1
    else:
      us+=0
      cs+=0
  
  print("Scores")
  if(us>cs):
    print(f"user is the winner with score {us}/{t}")
  elif(cs>us):
    print(f"computer is the winner with score {cs}/{t}")
  elif(cs==us):
    print("it's a draw")
  print()
  print("**********")
  r=input('''Would you like to play another round ?
  if yes type "y" , if no the type "n" :''')
print("game ended")
    
  
