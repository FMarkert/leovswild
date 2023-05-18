from actions import *
import random 




def chap4_0():
    from kap5 import chap5
    game = True
    global lifepoints

    print("\nKAPITEL 4\n")

    print('\nDu hast dich eine Viertelstunde mit dem Rücken an einen Baum gelehnt ans Ufer des kleinen Flusses gesetzt um wieder zu Kräften zu kommen. \n„Was für ein abgefuckter Tag, das muss ich später Bro erzählen.“ denkst du dir. ')
    print('\nBevor du aufstehst um nach Hause zu gehen siehst du dich noch ein wenig um: \nHinter dir befindet sich ein neuer Waldweg, du kannst also nicht allzu weit weg von der Zivilisation sein. \nNeben dem Waldweg liegen einige Baumstämme aufgestapelt. \nHier wurden wohl erst vor Kurzem Bäume gefällt. Du schaffst es aufzustehen, merkst aber wie sehr dir dein ganzer Körper wehtut. \nDas wird morgen extremen Muskelkater geben. ')
    print('\nDu gehst auf den Waldweg zu und bemerkst auffällige Reifenspuren von einem Traktor oder ähnlichem. \nIn diese Richtung muss das Holz wohl weggebracht werden und hier solltest du auch raus aus diesem Dreckswald kommen. ')
    print('\nDu atmest noch einmal tief durch, fühlst dich bereit für die Heimreise und wirfst noch mal einen letzten Blick in Richtung Fluss. \nDann traust du deinen Augen nicht: Von der anderen Seite des Flusses schwimmen mindestens 5 Wildschweine auf dich zu. \nPanisch versuchst du sofort den Waldweg als Fluchtroute zu nehmen aber aus den Gebüschen und hinter dem Holzstapel kommen noch mehr Wildschweine hervor und ehe du dich versiehst bist du komplett von Wildschweinen umzingelt. ')
    print('\n„Jetzt bin ich endgültig gefickt…“ denkst du dir. \nZwischen den anderen Wildschweinen tritt auf einmal ein besonders großer Keiler hervor und kommt langsam auf dich zu. \nDu könntest schwören, dass das Schwein mindestens so groß wie ein Kleinwagen ist und bist dir sicher, dass es sich hier um den Anführer der Wildschweine handelt. \nDein letztes Stündlein hat wohl geschlagen aber kampflos aufgeben willst du nicht. ')



    while game==True:
        if lifepoints==[]:
            game=False
            break
    
        antwort = ""
        antwort2 = ""
        antwort3= ""
        phase1 = 0
        phase2 = 0
        axt = 0

        while phase1==0:
            print('\nDas Alphaschwein kommt auf dich zu. \nWas willst du tun?\n')
            print(aktionen)
            antwort=input("Was machst du? ")
            if antwort==aktionen[0]: #umsehen
                print('\nDu siehst dich verzweifelt nach etwas womit du dich zur Wehr setzen kannst um. \nDie Stöcke und Steine am Boden vor dir sind zu klein um irgendwie Schaden zu verursachen und das riesige Schwein kommt langsam näher. \nDu hast dich schon fast mit deinem Schicksal abgefunden als du zwischen den aufgereihten Baumstämmen auf einmal etwas schimmern siehst. \nDas Wildschwein fängt an zu beschleunigen und wird dich jede Sekunde überrennen. \nMöchtest du nach dem schimmernden Etwas greifen?\n')
                print(ja_nein)
                phase1 +=1 
                antwort2=input('Aufheben? ')
                if antwort2 == ja_nein[1]: #ja
                    print('\nDu schaffst es nach dem Gegenstand zu greifen und ihn aus dem Baumstammstapel herauszuziehen. \nEs handelt sich tatsächlich um eine Holzfälleraxt, die wohl hier vergessen wurde. \n"Nur eine Kettensäge wäre jetzt noch besser gewesen." denkst du dir aber zumindest musst du jetzt nicht kampflos sterben. \n')
                    axt +=1 
                    antwort2=""
                    antwort =""
                    break
                elif antwort2==ja_nein[0]: #nein
                    print('Du nutzt die wenigen Sekunden, die dir bleiben lieber um auf den Angriff des Wildschweins zu reagieren. \n')
                    antwort2=""
                    antwort =""
                    break
                else:
                    print('Du sprichst die Sprache der Götter')
            elif antwort==aktionen[1]: #aufheben
                print('\nDu hebst einen kleinen Stein vom Boden auf und wirfst ihn dem großen Wildschwein auf die Schnauze. \nDas hat den Keiler noch wütender gemacht. \nDas Wildschwein fängt an zu beschleunigen und wird dich jede Sekunde überrennen.\n')
                phase1+=1
                antwort=""
                break
            elif antwort==aktionen[2]: #reden
                print('\n„Fick deine Mutter du kleiner Nuttensohn!!!“ schreist du. \nDanach folgen noch ein paar albanische Kraftausdrücke die du im Laufe deines Lebens aufgeschnappt hast. \nDer Wildschweinanführer zeigt sich davon eher unbeeindruckt… \nDas Wildschwein fängt an zu beschleunigen und wird dich jede Sekunde überrennen.\n')
                phase1+=1
                antwort=""
                break
            elif antwort==aktionen[3]: #fliehen
                print("\nEs gibt absolut keine Möglichkeit, wie du aus dieser Situation fliehen könntest. \nDas Wildschwein fängt an zu beschleunigen und wird dich jede Sekunde überrennen.\n")
                phase1+=1
                antwort=""
                break
            elif antwort==aktionen[4]: #nichts
                print('\nDu bist vor Angst wie gelähmt. \nDas Wildschwein fängt an zu beschleunigen und wird dich jede Sekunde überrennen.\n')
                phase1+=1
                antwort=""
                break
            else:
                print("Giggle... Wie bitte?")
    

        while phase2==0:
            print('\n Versuchst du auszuweichen?\n')
            print(ja_nein)
            antwort2=input('Ausweichen? ')
            if antwort2==ja_nein[0]: #nein
                if axt!=0:
                    print('\nDu hebst die Axt mit beiden Armen hinter deinen Kopf und wirfst sie anschließend mit deiner ganzen Kraft in Richtung des Wildschweins, welches direkt auf dich zu rennt. \nWarum du die Axt wirfst anstatt sie direkt in das Tier zu rammen kannst du dir nicht erklären. \nFakt ist aber, dass du den Wildschweinanführer mit der Klinge direkt zwischen die Augen triffst und er vor dir zu Boden geht. \n')
                    phase2+=1
                    game=False
                    chap5()
                    break
                else:
                    print('\nDas Wildschwein zerfetzt dich auf so üble Art und Weise, dass das hier aus Jungendschutzgründen nicht weiter ausgeführt werden kann. \n')
                    youdied()
                    antwort2=""
                    break
            elif antwort2==ja_nein[1]: #ja
                print('\nDu schaffst es tatsächlich dem Angriff des Wildschweins mit einem Sprung zu Seite auszuweichen und es rennt an dir vorbei. \nDu kommst wieder auf die Beine während sich das Wildschwein wieder zu dir wenden will um den nächsten Angriff zu starten. \nJetzt ist die wahrscheinlich letzte und einzige Chance dich irgendwie zu wehren. \nMöchtest du versuchen das Wildschwein anzugreifen?\n')
                print(ja_nein)
                antwort3=input("Angreifen? ")
                if antwort3==ja_nein[0]: #nein
                    print("\nDas Wildschwein rennt wieder auf dich zu und zerfetzt dich auf so üble Art und Weise, dass das hier aus Jungendschutzgründen nicht weiter ausgeführt werden kann. \n")
                    youdied()
                    antwort3=""
                    break
                elif antwort3==ja_nein[1]: #ja
                    if axt!=0:
                        print('\nDu hebst die Axt mit beiden Armen hinter deinen Kopf und wirfst sie anschließend mit deiner ganzen Kraft in Richtung des Wildschweins, welches direkt auf dich zu rennt. \nWarum du die Axt wirfst anstatt sie direkt in das Tier zu rammen kannst du dir nicht erklären. \nFakt ist aber, dass du den Wildschweinanführer mit der Klinge direkt zwischen die Augen triffst und er vor dir zu Boden geht. \n')
                        phase2+=1
                        game=False
                        chap5()
                        break
                    else: 
                        print('\nEs geht jetzt um alles oder nichts… \nDie einzige Möglichkeit aus dieser Situation zu entkommen ist deine mächtigste Fähigkeit einzusetzen. \nEine Fähigkeit, die in deiner Familie schon seit vielen Jahrhunderten von Generation zu Generation weitergereicht wird: Der Schwitzkasten des Todes. \nDu hast dir eigentlich geschworen, diese Fähigkeit nie wieder gegen einen Menschen einzusetzen. \nVor dir steht allerdings ein großes Schwein, von daher ist das vollkommen ok. \nDu breitest also die Arme aus, gehst leicht in die Knie und versuchst das auf dich zu rennende Wildschwein am Hals zu packen.\n')
                        chance=random.uniform(0,1)
                        if chance >=0.6:
                            print('\nDas riesige Wildschwein und du rennt aufeinander zu. \nDie Situation kommt dir vor wie in Zeitlupe. \nDu springst auf das Tier und umschlingst es am Hals mit deinen Armen. \nDer Wildschweinanführer kommt dir auf einmal nicht mehr so groß wie ein Kleinwagen vor, eher so groß wie ein mittelgroßer Hund. \nDas Adrenalin, das dir durch den Körper schießt mobilisiert deine letzten Kraftreserven und du würgst das Tier so hart im Schwitzkasten des Todes bis es zu Boden geht und sich nicht mehr rührt. \n')
                            phase2+=1
                            game=False
                            chap5()
                            break
                        else:
                            print('\nWas hast du dir dabei eigentlich gedacht, Bro? \nEben kam dir das Schwein noch so groß wie ein Kleinwagen vor und jetzt willst du es in den Schwitzkasten nehmen?!?! \nDas Wildschwein zerfetzt dich auf so üble Art und Weise, dass das hier aus Jungendschutz nicht weiter ausgeführt werden kann. \n')
                            youdied()
                            antwort3=""
                            break
                else:
                    print("\nDu nimmst die deutsche Sprache und brichst sie... \nEin einfaches 'ja' oder 'nein' reicht mir.\n")
                    