# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:17:22 2020

@author: anhtai
"""
import random 

"""f = open("sowpods.txt","r")
a = random.choice(f)
print(a)"""
#Reading text----
def openW():
    with open("sowpods.txt") as guess:
            word = list(guess)
    a = random.choice(word)
    a = a.strip()
    listA = a
    print(a)
    listB = [_ for _ in range(len(a))]
    for i in listB:
        listB[i] = "*"
    return listA , listB



counter = 0
#Introduction -- - -- - -    
def Introduction():
    
    print("Welcome to hangman game")
    print("Do you want to play - (Y/N)") 
    Ask_User()   
    
#Ask User    
def Ask_User():    
    global counter
    intro_input = str(input().upper())
    if intro_input == "Y":
        listA, listB = openW()
        print("Your word has " + str(len(listB)) + " letter" )
        print("".join(listB))
        
        while(counter < 6 and Check(listB) == False):
            CheckWord(listA,listB)        
        if counter<6:
            print("You win")
            counter = 0
            print()
            return Introduction()
        else:    
            print("You loose")
            print()
            return Introduction()
    elif intro_input == "N":
        print("Goodbye - see you next time")
    else:
        print("Please enter (Y) for Yes and (N) for No")
        return Ask_User()  
    
#Check********
        
def Check(listW):
    return (all(i != "*" for i in listW))


def CheckWord(listWord, listCount):
    global counter
    
    inp = str(input().upper())
    while len(inp) > 1:
        print("Please enter one letter")
        inp = str(input().upper())
    
        
    #lit = list(listWord)
    if inp in listWord:
        for i in range(len(listWord)):
            if inp == listWord[i]:
                listCount[i] = inp
                
                #listWord[i] = "*"
                #print(listWord)
                #print(listCount)
        listCount= "".join(listCount)   
        print(listCount)
        print("Good job!!!")
    else:
        counter += 1
        a = 6 - counter
        if a >0:
            print("You fail - Please try again - You still have " + str(a) + " time(s)" )
        else:
            print("Your friend was dead...")
            
Introduction()
     


            


 