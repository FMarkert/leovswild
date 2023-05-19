from actions import *


def chap1():

    from kap2_0 import chap2_0      

    print_slowly("\nKAPITEL 1\n\n")
    game=True
    
    global lifepoints  
    print_slowly("Du wachst an einem Sonntagnachmittag an einem wunderschönen sonnigen Frühlingstag auf und betrachtest dich im Spiegel. \n\nDer Winter war lang und hart und du fasst den Entschluss, dich endlich wieder in Form zu bringen. \n\n")

    print_slowly("Starten möchtest du deine große Transformation mit einer Runde Joggen im Wald. \nDu wirfst dich in deinen Jogginganzug, machst dir Kopfhörer rein und verlässt das Haus in Richtung des nahegelegenen Waldes.\n\n")

    print_slowly("Die Sonne scheint durch die Baumkronen, Vögel zwitschern und die Luft ist frisch. \nAls du tiefer in den Wald eindringst, bemerkst du, dass sich die Umgebung immer dichter verändert.\n")

    print_slowly("Der Wald wird dichter und unheimlicher und du hörst seltsame Geräusche um dich herum. \n\nDu spürst, wie sich eine leichte Unruhe in dir ausbreitet. \nAber bevor du Zeit hast, darüber nachzudenken, entdeckst du am Wegrand plötzlich einen Fuchs.\n")

    print_slowly("\n\nWie verhältst du dich?\n")
    
    
    
    while game == True:

        if lifepoints==[]:
                    game=False
                    break

        antwort = ""
  
        
        
        while antwort not in aktionen:

            print(aktionen)
            antwort = input("Was machst du? ")
            if antwort == aktionen[0]:#umsehen
                print_slowly("\nDu bemerkst, dass der Fuchs Schaum vor dem Mund hat und irgendwie krank aussieht.\n")
                antwort = ""
            elif antwort == aktionen[2]: #reden
                print_slowly('\n„Verpiss dich du Hundesohn“ schreist du. \nDer Fuchs zuckt bei der Lautstärke deiner Stimme zusammen und legt die Ohren nach hinten. \nEr antwortet dir allerdings nicht. Was erwartest du auch?\n')
                antwort = ""
            elif antwort == aktionen[1]: #aufheben
                print_slowly("\nAls du versuchst den Fuchs hochzuheben beißt er dir in deine Hand.\nDer Biss ist sehr schmerzhaft und blutet stark.\nDu schaffst es noch nach dem Fuchs zu treten aber der Fuchs rennt weg und du machst dich auf den Weg nach Hause. \nAuf dem Weg fühlst du dich immer schwächer bis du irgendwann zusammenbrichst. \nDir wird klar, dass der Fuchs Tollwut hatte.\n")
                youdied()
                break
            elif antwort == aktionen[4]: # nichts
                print_slowly("\nDer Fuchs nähert sich dir und du denkst dir nichts Böses dabei.\nPlötzlich schnappt der Fuchs zu und beißt dir in die Wade. \nDer Biss ist sehr schmerzhaft und blutet stark.\nDu schaffst es noch nach dem Fuchs zu treten aber der Fuchs rennt weg und du machst dich auf den Weg nach Hause. \nAuf dem Weg fühlst du dich immer schwächer bis du irgendwann zusammenbrichst. \nDir wird klar, dass der Fuchs Tollwut hatte.\n")    
                youdied()
                break
            elif antwort == aktionen[3]: #fliehen
                print_slowly("\nDer Fuchsbastard ist dir nicht geheuer und du legst einen ordentlichen Sprint hin bis dir die Puste ausgeht. \nMit hochrotem Kopf drehst du dich um und der Fuchs ist nicht mehr zu sehen. \nDu scheinst ihn abgehängt zu haben und gehst den Waldweg weiter entlang bis dein Puls sich wieder runtergefahren hat.\n\n")
                chap2_0()
                game=False
                antwort = ""
                break
            else:
                print_slowly("\nIch verstehe nicht was du mir sagen willst...\n")

    
            

        
       
            