'''
Program: Screens.py
Author : Stephanie Torres
Date   : 2019-11-04
Synopis: This contain all the screens and run them
'''
import os

def Scr_100(): #info screen
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print(" ")
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                       Welcome to the Enigma Machine!                         *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                       This is the software version of                        *")
    print("*                       the Enigma Machine used in WWII.                       *")
    print("*                                                                              *")
    print("*                       For when you have something                            *")
    print("*                       that needs hiding or cracking!                         *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")
    print("Press Enter to continue") 
    sel = input("")
    #import screen_MAIN
    #screen_MAIN.getOption("Home")
    return sel

def Scr_101(): #welcome screen
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Welcome"))
    print("")
    print("                              Encrpyt           1")
    print("                              Decrypt           2")
    print("                              Menu              3")
    print("                              Help              4")
    print("                              Exit              5")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Please make a selection.")

    if sel == "1":
        os.system("clear")
        Scr_113() #encryption screen
    if sel == "2":
        os.system("clear")
        Scr_114() #decryption screen
    if sel == "3":
        os.system("clear")
        Scr_102() #menu
    if sel == "4":
        os.system("clear")
        Scr_110() #settings
    if sel == "5":
        os.system("clear")
        Scr_115() #exit
  #  else:
  #      os.system("clear")
  #      Scr_112() #error

    return sel



def Scr_102(): #menu
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Menu"))
    print("")
    print("				 Setting    1")
    print("				 Help       2")
    print("				 ")
    print("{:^80}".format("Go Back  [x]"))
    print("				    	")
    print("		")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    if sel == "1":
        os.system("clear")
        Scr_103() #setting
    if sel == "2":
        os.system("clear")
        Scr_110() #help
    if sel == "x":
        os.system("clear")
        Scr_101() #welcome screen
    ##else:
      ##  os.system("clear")
      ##  Scr_112() #error

    return sel

def Scr_103(): #setting screen
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Settings"))
    print("")
    print("			   Change Rotors            1")
    print("                           Change Plug Board        2")
    print("                           Change Key    	    3")
    print("			   ")
    print("{:^80}".format("Go Back  [x]"))
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    if sel == "1":
        os.system("clear")
        Scr_104()#rotor settings
    if sel == "2":
        os.system("clear")
        Scr_108()# plugboard settings
    if sel == "3":
        os.system("clear")
        Scr_109()#key settings
    if sel == "x":
        os.system("clear")
        Scr_101() #welcome screen
    #else:
     #   os.system("clear")
      #  Scr_102() #menu screen

    return sel

def Scr_104(): #rotor screen (not in Quangs version)
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("			   	Select which rotor you ")
    print("				would like to change.")
    print("			    ")
    print("			         Rotor 1	      1")
    print("			         Rotor 2	      2")
    print("			         Rotor 3	      3")
    print("			         ")
    print("{:^80}".format("Go Back  [x]"))
    print("				 ")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor settings: ")
    
    if sel == "1":
        os.system("clear")
        Scr_105()#rotor-1 settings
    if sel == "2":
        os.system("clear")
        Scr_106()# rotor-2 settings
    if sel == "3":
        os.system("clear")
        Scr_107()#rotor-3 settings
    if sel == "x":
        os.system("clear")
        Scr_103() #setting screen
   # else:
    #    os.system("clear")
     #   Scr_102() #menu screen
    return sel

def Scr_105(): #rotor-1 settings
    print("CIS220 Project:TheEnigmaMachine               Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Change Rotor-1"))
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("			   ")
    print("{:^80}".format("Go Back  [x]"))
    print("			    ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")

    # missing info once you make slection or automatically changes in back housing

    if sel == "1":
        os.system("clear")
        Scr_112()#rotor-A
    if sel == "2":
        os.system("clear")
        Scr_112()# rotor-B
    if sel == "3":
        os.system("clear")
        Scr_112()#rotor-C
    if sel == "4":
        os.system("clear")
        Scr_112()# rotor-D
    if sel == "5":
        os.system("clear")
        Scr_112()#rotor-E
    if sel == "x":
        os.system("clear")
        Scr_104() #rotor settings
    return sel


def Scr_106(): #rotor-2 settings
    print("CIS220 Project:TheEnigmaMachine               Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Cahnge Rotor-2"))
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("			")
    print("{:^80}".format("Go Back  [x]"))	    
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")
    # missing info once you make slection or automatically changes in back housing

    if sel == "1":
        os.system("clear")
        Scr_112()#rotor-A
    if sel == "2":
        os.system("clear")
        Scr_112()# rotor-B
    if sel == "3":
        os.system("clear")
        Scr_112()#rotor-C
    if sel == "4":
        os.system("clear")
        Scr_112()# rotor-D
    if sel == "5":
        os.system("clear")
        Scr_112()#rotor-E
    if sel == "x":
        os.system("clear")
        Scr_104() #rotor settings
    return sel

def Scr_107(): #rotor-3 settings
    print("CIS220 Project:TheEnigmaMachine               Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Change Rotor-3"))
    print("				")
    print("			    Rotor A		    1    ")
    print("			    Rotor B		    2")
    print("			    Rotor C		    3")
    print("			    Rotor D		    4")
    print("			    Rotor E		    5")
    print("			    ")
    print("{:^80}".format("Go Back  [x]"))
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to change rotor: ")
    # missing info once you make slection or automatically changes in back housing
    if sel == "1":
        os.system("clear")
        Scr_112()#rotor-A
    if sel == "2":
        os.system("clear")
        Scr_112()# rotor-B
    if sel == "3":
        os.system("clear")
        Scr_112()#rotor-C
    if sel == "4":
        os.system("clear")
        Scr_112()# rotor-D
    if sel == "5":
        os.system("clear")
        Scr_112()#rotor-E
    if sel == "x":
        os.system("clear")
        Scr_104() #rotor settings
    return sel


##PLUGBOARD IS MISSING CALL AFTER SCRIPT IS EXECUTED

def Scr_108(): #plugboard settings
    import Plugboard
    print("CIS220 Project:TheEnigmaMachine                 Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Plug Board"))
    print("				")
    print("		            To change your plugbaord ")
    print("		            please enter a new plugboard ")
    print("		            name at the bottom.     ")
    print("			   ")
    print("{:^80}".format("Go Back  [x]"))
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Enter your new plugboard name here or press X to return to previous menu: ")
    if sel == "x":
        os.system("clear")
        Scr_103() #settings
    return sel

##KEY IS MISSING CALL AFTER SCRIPT IS EXECUTED

def Scr_109(): #key setting
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Key"))
    print("				")
    print("{:^80}".format("Enter your key below"))
    print("			    ")
    print("{:^80}".format("Go Back  [x]"))
    print("			    ")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Enter Key:    ")
    return sel


def Scr_110(): #help
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Help"))
    print("")
    print("			   Instructions		1")
    print("		           Info 		2")
    print("                         ")
    print("{:^80}".format("Go Back  [x]"))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Please enter a number.")

    if sel == "1":
        os.system("clear")
        Scr_111() #instructions
    if sel == "2":
        os.system("clear")
        Scr_119() #info
    if sel == "x":
        os.system("clear")
        Scr_102() #menu

    return sel


def Scr_111(): #Instructions (not in Quangs version)
    print("CIS220 Project:TheEnigmaMachine                 Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Instructions"))
    print("")
    print("		Input text in the input box                        ")
    print("		Press the Enter button to encrypt text               ")
    print("		Wait for a second to get the encrypted text	   ")
    print("		Choose an option once your message is encrypted            ")
    print("		press exit if you want to end the program           ")
    print("")
    print("")
    print("")
    print("               Home  [1]                      Exit [2]")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")
    if sel == "1":
        os.system("clear")
        Scr_101()
    if sel == "2":
        os.system("clear")
        Scr_115()
    return sel

def Scr_112(): #error (not in Quangs Version)
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Error"))
    print("")
    print("	                     Oops! You have reached an error.")
    print("		             Please select an option below. ")
    print("")
    print("                                 Help           1")
    print("                                 Menu       2")
    print("                                 Exit           3")
    print("                                 ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Select a number to proceed: ")

    if sel == "1":
        os.system("clear")
        Scr_110() #help
    if sel == "2":
        os.system("clear")
        Scr_102() #menu
    if sel == "3":
        os.system("clear")
        Scr_115() #exit

    return sel




def Scr_113(): #encyption
    key = Scr_116()
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("{:^80}".format("Encryption"))
    print("")
    print("{:^80}".format("Enter your message below"))
    print("{:^80}".format("Key: " + key))
    print("")
    print("            ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Enter Message:  ")
    return sel


def Scr_114(): #decryption 
    key = Scr_117()
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("{:^80}".format("Decryption"))
    print("")
    print("{:^80}".format("Enter your message below"))
    print("{:^80}".format("Key: " + key))
    print("")
    print("            ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("Enter Message:  ")
    return sel


def Scr_115(): #exit
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("                                 ")
    print("{:^80}".format("The End"))
    print("			   	  ")
    print("{:^80}".format("Thank you for using our"))
    print("{:^80}".format("software version of the "))
    print("{:^80}".format("WWII Enigma Machine."))
    print("			    ")
    print("			    ")
    print("			    ")
    print("					")
    print("					")
    print("						")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    sel = input("")
    return sel


def Scr_116(): #encryption key
    
    from generateKey import getKey
    print("CIS220 Project:TheEnigmaMachine                 Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Encryption"))
    print("")
    print("{:^80}".format("Enter your key or hit Enter to generate key"))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    key = input("Enter Key:  ")

    if key == '':
        key = getKey()
    xkey = ''
    for i in key:
        xkey = xkey + str(i)
    key = xkey    
    return key

def Scr_117(): #decryption key
    
    from generateKey import getKey
    print("CIS220 Project:TheEnigmaMachine                 Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Decryption"))
    print("")
    print("{:^80}".format("Enter your key or hit Enter to generate key"))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    key = input("Enter Key:  ")
    
    if key == '':
        key = getKey()
    xkey = ''
    for i in key:
        xkey = xkey + str(i)
    key = xkey    
    return key

def Scr_118(doc): #message (doc)
    print("CIS220 Project:TheEnigmaMachine                 Programmers: CIS220 Class Fall 2019")
    print("")
    print("")
    print("")
    print("{:^80}".format("Enigma Machine"))
    print("")
    print("")
    print("{:^80}".format("Message"))
    print("")
    mtyLine = 13 - len(doc)
    for i in doc:
        print(i, end='')
    for i in range(mtyLine):
        print("")
    print("")
    sel = input("Choose an option to proceed: ")
    return sel

def Scr_119(): #help info screen
    print("CIS220 Project:TheEnigmaMachine              Programmers: CIS220 Class Fall 2019")
    print(" ")
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                       Welcome to the Enigma Machine!                         *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                       This is the software version of                        *")
    print("*                       the Enigma Machine used in WWII.                       *")
    print("*                                                                              *")
    print("*                       For when you have something                            *")
    print("*                       that needs hiding or cracking!                         *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")
    print("Press Enter to continue")  
    sel = input("")
    import Screens
    #Screens.getOption("")
    return sel



## MAIN


os.system("clear")
Scr_100()
os.system("clear")
Scr_101()
