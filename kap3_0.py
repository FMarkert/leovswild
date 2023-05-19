from actions import *



def chap3_0():
    print_slowly("\nKAPITEL 3\n\n")
    from kap3_1 import chap3_1
    game=True
    umsehen = 0 #Hilfsvariable
    global lifepoints


    print_slowly("\nDu bist weiter abseits des Waldweges unterwegs und joggst über Stock und Stein. \nDu nimmst einen würzigen Geruch wahr, der dich fast ein bisschen an Maggi erinnert und deine Gedanken schweifen ab in Richtung Abendessen. \n\nHeute soll es Dorschrogen geben, dazu selbstgemachten Knoblauchsalat mit roter Beete und Mayonnaise. \nAbgerundet wird das ganze mit Weintrauben und Gummibärchen. \nBei dem Gedanken läuft dir das Wasser im Mund zusammen…\n\n")
    print_slowly("Plötzlich wird dein Tagtraum unterbrochen als du vor dir auf einmal ein Grunzen wahrnimmst. \nVor dir steht ein ausgewachsenes Wildschwein und es starrt dir direkt in die Augen. \nIm gleichen Moment nimmst du wahr, dass sich um dich herum noch mindestens 3 andere ausgewachsene Wildschweine befinden. \nZudem siehst du hinter dem Wildschwein, welches direkt vor dir steht noch mehrere Frischlinge mit ihrem hellbraun und dunkelbraun gestreiftes Fell panisch von Busch zu Busch rennen. \n\nWie reagierst du?\n")


    while game==True:
        if lifepoints==[]:
                    game=False
                    break

        antwort = ""
        

        while antwort not in aktionen:
            print(aktionen)
            antwort = input("Was machst du? ")

            if antwort == aktionen[0]: #umsehen
                if umsehen == 0:
                    print_slowly('\nViel Zeit zum Umsehen bleibt dir nicht… \nVor dir ist die Wildschweinherde die dich innerhalb der nächsten Sekunden angreifen wird, wenn du nichts unternimmst. \nDie Tiere geben dir mit ihrem Manöver zu verstehen, dass du dich sofort verpissen sollst. \nZu deiner Rechten geht es bergauf und das Gebiet wird felsiger. Zu deiner Linken hörst du ein leises Rauschen. \nDu weißt, dass ein kleiner Fluss durch den Wald fließt, welcher ungefähr in der Richtung liegen müsste. \nNach hinten schauen möchtest du nicht, da du den Tieren nicht den Rücken zudrehen willst. \nWas machst du also?\n')
                    umsehen +=1
                    antwort=""
                    
                else:
                    print_slowly("\nKein guter Zeitpunkt um einfach nur dumm rumzustehen… \nVon hinten rammt ein Wildschweinschädel gegen deine Beine wirft dich zu Boden… \nJetzt attackieren dich auch die restlichen Tiere. \nDu bist gefickt…")
                    youdied()
                    antwort=""
                    break
            elif antwort == aktionen[1]: #aufheben
                print_slowly("\nDu versuchst nach einem der Schweine zu greifen und schaffst es tatsächlich eines hochzuheben. \nVon hinten rammt allerdings ein anderes Wildschwein gegen deine Beine wirft dich zu Boden… \nJetzt attackieren dich auch die restlichen Tiere. \nDu bist gefickt…\n")
                youdied()
                antwort=""
                break
            elif antwort == aktionen[2]: #reden
                print_slowly('\nDu schreist die Tiere an um sie zu verscheuchen. \nDie Tiere werden aufgescheucht und setzen sich in Bewegung. \nVon hinten rammt ein Wildschweinschädel gegen deine Beine wirft dich zu Boden… \nJetzt attackieren dich auch die restlichen Tiere. \nDu bist gefickt…\n')
                youdied()
                antwort=""
                break
            elif antwort == aktionen[3]: #fliehen
                print_slowly('\nDir gehen in diesem Moment ganz klare Gedanken durch den Kopf: \n„Wenn ein Wildschwein wegrennt, ist es in Ordnung. \nBleibt es aber stehen und beobachtet dich, dann weißt du, dass du ganz falsch bist und wahrscheinlich in der Nähe von ihrem Platz.“\nDir ist bewusst, dass du am Arsch bist wenn du stehen bleibst. \nAlso machst du dich bereit zum Abhauen. \nIn welche Richtung rennst du?\n')
                game=False
                chap3_1()
                break
            elif antwort == aktionen[4]: #nichts
                print_slowly("\nKein guter Zeitpunkt um einfach nur dumm rumzustehen… \nVon hinten rammt ein Wildschweinschädel gegen deine Beine wirft dich zu Boden… \nJetzt attackieren dich auch die restlichen Tiere. \nDu bist gefickt…")
                youdied()
                antwort=""
                break
                
            else:
                print_slowly("\nIch verstehe nicht was du mir sagen willst...\n")
                antwort=""
                

        

    


                  
            
                

