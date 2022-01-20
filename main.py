import requests
import json
import datetime
import random 
import os
total = 5
def the_game():
    num = random.randint(1,6236)
    r = requests.get(f"http://api.alquran.cloud/v1/ayah/{num}")
    Ayah_data=r.json().get('data').get('surah').get('number')
    text=r.json().get('data').get('text')
    juz=r.json().get('data').get('juz')
    print(Ayah_data)
    print(text)
    flag = True
    half_flag = True
    while flag == True:
        global total
        try:
            Guessed_a = int(input("Please Guess Number of the surah in which the ayah locates \n"))
        except :
            print("Sorry, invalid input")    
        if half_flag == True: 
            if Guessed_a == Ayah_data :
                print("Good Job!!!")
                total = total+2
                the_game()
            else:
                wanna = input("Wrong guess. Try again by pressing T or use a hint by pressing H. To quit, press Q \n").lower()  
                if wanna == "t":                    
                    half_flag = True;
                if wanna == "n" :  
                    print("let's start again") 
                    the_game() 
                elif wanna == "h":
                    total = total-1
                    print(f" Juzz is in is located in Juz --> {juz}")
                elif wanna == "q":
                    print(f"Your score is {total}")
                    os._exit(0)
the_game()
        

