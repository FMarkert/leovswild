#Grundlegende Befehle für alle Kaptiel



ja_nein = ["nein","ja"]

richtungen = ["vorne","links","rechts","hinten"]

aktionen = ["umsehen","aufheben","reden","fliehen","nichts"]

lifepoints = ["heart","heart","heart,heart,heart"]



def checklife(): #prüft lebensleiste
   global lifepoints
   print(f"\nDu hast noch {len(lifepoints)} Leben übrig, Bro\n")
  
      

def youdied(): #löscht 1 Leben und checkt ob noch welche über sind
    global lifepoints
    print("\nBro, du bist gestorben...\n")
    if len(lifepoints)>0:
        lifepoints.remove("heart")
    checklife()
    if len(lifepoints)==0:
        print("\nGAME OVER\n")
        
import sys,time

def print_slowly(str): #angepasste formel aus dem Internet, um Textausgabe zu verlangsamen und "tippen" zu simulieren
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


    
       

    
         

    

      
      
    
