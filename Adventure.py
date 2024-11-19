str = " \033[42;1;91m NOT SOO EPIC GAME PRESENTS \033[m "
str2 = "  \033[1;91m THE ADVENTURE GAME  \033[m "
life = 3

#Starting of the game

print("|{: ^100}|\n".format(str))
print("|{:*^100}|\n".format(str2))

#Asking user if it wants to take participate in game or not

a = input(("DO YOU WANT TO TAKE PART IN THE ADVENTURE (\033[32;1myes\033[m/\033[91;1mno\033[m)? ")).lower()

if a=="yes":
   pass
else:
    quit()
any =True
name = input("\nEnter your name : ")
print("\033[2J\033[H", end="")  #used for clearing th eterminal
print("|{:*^100}|\n".format("| INSTRUCTIONS |"))
print(name.upper(),"this Adventure consist of various levels you have only three lives you will encounter various tasks on the way Best of Luck for your journey\n")
print(" O","A",sep="     ->")
print("/|\\")
print("/ \\")

print("\n/O\\","B",sep="    ->")
print("/|\\")
print("/ \\")

#choosing character

choose_char=True


while choose_char:
 char = input("\nEnter your character : ").lower()
 print("\033[2J\033[H", end="")
 if char=="a":
    print(" O")
    print("/|\\")
    print("/ \\",end=f"   \n\n{name} Get ready for the Adventure\n\n")
    choose_char=False
 elif char=="b":
    print("/O\\")
    print("/|\\")
    print("/ \\",end=f"  \n {name} Get ready for the Adventure\n\n")
    choose_char=False
 else:
    print("invalid choice")
    
    #Starting of main game
    
print("|{:?^100}|\n".format(" | You Are awake from a deep sleep.......Phone near you is ringing....... |"))
ans = input("Answer the phone call?\033[32m yes\033[m / \033[91m no\033[m : ").lower()
print( )
if ans=="yes":
    while any:
          a=input("Captain : 'Hellow sargent, this is captain speaking you have to get that precious stone from that forest,are you ready for the challenge:\n A)Yeah sure i will do my best   B)Naa I am done!' :\n ").lower()
          print("\033[2J\033[H", end="")
          if a=="a":
            print("|{:*^80}|".format(" Great Best Of Luck "))
            any=False
          else:
            print("|{:*^100}|".format(" You Lose a Life.... "))
            life-=1
            if life>0:
               print(f"You have {life} life left")
            else:
               print("You loose You loose all your life.....")
               quit()
    print("Narrator : 'You start to search for that stone and encounter your first challenge'\n")
    
    #first challenge
    
    print(f"Stranger : 'Where are you going {name}, you look in a hurry , you first have to defeat me'")
    if char=="a":
      print(" O")
      print("/|\\")
      print("/ \\")
    elif char=="b":
      print("/O\\")
      print("/|\\")
      print("/ \\")
    print("\033[91;1m\n<-O->","\/|\/"," / \\\033[m",sep="\n")  
    
    
    fig = True
    
    #loop for the options accordingly 
   
    while fig :
          fight = input("A punch is incoming hurry up!!! A) 'Duck' B)'Puch' : ").lower()
          print(  )
          if fight=='b':
            print("|{:*^130}|".format("\033[91;1mOops opponent hits you first you loose a life\033[m"))
            print("\033[91;1m<-O->","\/|\/"," / \\\033[m",sep="\n")
            print("O",end="")
            print("/",end="")
            print("---",end="")
            print("\\")
            life-=1
            if life>0:
               print(f"You have {life} life left")
            else:
               print("You loose You lost all your life.....")
               quit()
          elif fight=='a':
            print("|{:*^100}|".format(" \033[32;1mYou duck successfully and opponent hits his arm on the tree and broke his arms , You Win!!\033[m "))
            fig=False
            if char=="a":
               print(" O")
               print("/|\\")
               print("/ \\")
            elif char=="b":
               print("/O\\")
               print("/|\\")
               print("/ \\")
            print("\033[91;1m<-O->","/","---\033[m")
          
        
          else:
             print("Invalid choice!!!")
    print(  )
    
    #Second challenge 
    
    print("Now its evening time and you will be dead in this forest at night so you have to find a shelter")
    print( )
    hut=True
    while hut:
        light = input("A light is coming from a far source should I check? A)\033[32myes\033[m  B)\033[91mno\033[m : ").lower()
        print("\033[2J\033[H", end="")
        if light=="b":
             print("|{:*^100}|".format(" Night arrives and animal kill you "))
             life-=1
             if life>0:
               print(f"You have {life} life left")
             else:
               print("You loose You lost all your life.....")
               quit()

        elif light=="a":
               print("Stranger : 'Hellow my dear if you want to use this hut you first need to defeat me in Rock/Paper/Scissors Game")
               
               #rock paper game using random
               
               import random
               play=True
               while play:
                 
                 print( )
                 user=input("Enter Your Choice (\033[90mrock\033[m/\033[92mpaper\033[m/\033[96mscissors\033[m): ").lower()
                 myChoice =random.choice(["rock","paper","scissors"])
                 if (user == "rock" and myChoice == "scissors") or \
                 (user == "paper" and myChoice == "rock") or \
                 (user == "scissors" and myChoice == "paper"):
                  print("\033[2J\033[H", end="")  
                  print("\033[92mYou win!\033[m You can stay in this hut....")
                  play = False 
                  hut=False
                 elif (user == "rock" and myChoice == "paper") or \
                    (user == "paper" and myChoice == "scissors") or \
                    (user == "scissors" and myChoice == "rock"):
                    print("\033[91mYou loose..!\033[mtry again.")
                    life -= 1
                    if life>0:
                      print(f"You have {life} life left")
                    else:
                      print("You loose You lost all your life.....")
                      quit()       
                 elif user==myChoice:
                   print("It is a tie play again....")
        
        
        #Third challlenge (answer is footsteps)
        
    print("\n|{:*^80}|\n".format(" The Morning arrives You continue with your journey "))
    print("On your way you find a wise old man\n")
    print("\033[1m  /O\\","|\/|\\","| / \\\033[m",sep="\n")
    print("\nQld man: 'Hellow young man you must be searching for the precious stone i can give you  that but first you have to answer my queston\n")
    q = True
    while q:
         ques =input("|{:*^100}|\n".format(" Old man: \033[96;1m'The more you take,the more you leave behind .What am I?'\033[m "))
         print("\033[2J\033[H", end="")
         if ques=="footsteps":
            print("Old man: 'You are right, as i promised here is the stone you need")
            print( )
            if char=="a":
                  print("\033[1m  /O\\    O","|\/|\/*\/|\\","| / \   / \\\033[m",sep="\n")
            elif char=="b":
                  print("\033[1m  /O\\   /O\\","|\/|\/*\/|\\","| / \   / \\\033[m",sep="\n")
            q =False
         else:
            print("You lost a life")
            life-=1
            if life>0:
               print(f"You have {life} left")
            else:
               print("You loose.... You lost all your life.....")
               quit()
    print(  )
    if life>0:
        
        print("|{:*^100}|".format("\033[92;1m You Win..\033[m "))
    else:
        print("\033[91;1mYou loose.... You lost all your life.....\033[m")
        quit()
    print( )
else:
   
   #second part for the future projects
   
    print("Uthaa lete phone yaar bichaara koi call karra...... Uthao dobara run karke")
print("#"*100,"\n\nMade By : Krishna\nPlayed By :",name,"\nLanguage Use : Python\nThank You for Playing  ^v^\n","\033[1B \033[51D","#"*100 ,sep=" " )

