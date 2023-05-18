from actions import *
from random import random



def chap3_1():
    from kap4_0 import chap4_0
    game=True
    global lifepoints 



    while game==True:
            if lifepoints==[]:
                        game=False
                        break
            print("In welche Richtung möchtest du fliehen? ")
            antwort = ""
            antwort2 = ""

            while antwort not in richtungen:
                    print(richtungen)
                    antwort = input("In welche Richtung gehst du? ")

                    if antwort==richtungen[0]: #vorne
                            print('Du rennst geradeaus auf die Wildschweine zu. \nDumme Idee! \nDie Tiere sehen das als Angriff und tun alles um ihren Nachwuchs zu beschützen. \nDu wirst von mehreren Seiten aus attackiert und gehst zu Boden.\n')
                            youdied()
                            antwort =""
                            break
                    elif antwort==richtungen[1]: #links
                            print("Du sprintest so schnell du kannst nach links. \nWie du bereits vermutet hast stößt du nach kurzer Zeit auf einen kleinen Fluss. \nDas Grunzen hinter dir kommt immer näher. \nMöchtest du in den Fluss springen?\n")
                            antwort2=input("In den Fluss springen? ")
                            if antwort2 == ja_nein[1]: #ja
                                    print("Du springst in den Fluss. \nDie Strömung treibt dich ein ganzes Stück mit aber du schaffst es trotzdem ans andere Ufer zu gelangen. \nVon deinen Verfolgern fehlt jegliche Spur. Sie müssen aufgegeben haben. \nAm Flussufer legst du dich erst mal auf den Boden und versuchst wieder zu Atem zu kommen. \n")
                                    game=False
                                    chap4_0()
                                    break
                            else: #nein
                                    print("Du wirst von mehreren Wildschweinen attackiert und gehst zu Boden.\n")
                                    youdied()
                                    break
                    elif antwort==richtungen[2]: #rechts
                            print("Du sprintest so schnell du kannst nach rechts und bemerkst, dass das Gelände um dich herum immer felsiger wird. \nDu kommst ohne zu stolpern gut voran und glaubst, deine Verfolger fast abgehängt zu haben. \nNach kurzer Zeit stößt du allerdings auf eine kleine Felswand und realisierst, dass diese zu steil zum Hochklettern ist. \nHinter dir versammeln sich die Wildschweine. \nDie einzige Möglichkeit, die du noch siehst, ist an der Felswand entlang zu laufen bis du mit etwas Glück einen Bogen um die Schweine machen kannst. \nWillst du es versuchen?")
                            print(ja_nein)
                            antwort=input("Versuchen einen Bogen zu machen? ")
                            if antwort2 == ja_nein[1]: #ja
                                antwort2=""
                                chance = random.uniform(0,1)
                                if chance >= 0.4:
                                    print("Ja: Du schaffst es tatsächlich einen Bogen um die dich verfolgende Herde zu machen. \nDu bist eigentlich schon längst an deinen körperlichen Grenzen aber das Adrenalin lässt dich weiter rennen bis du irgendwann auf einen kleinen Fluss stößt. \nDu siehst keine andere Möglichkeit mehr und springst hinein. \nDie Strömung treibt dich ein ganzes Stück mit aber du schaffst es trotzdem ans andere Ufer zu gelangen. \nVon deinen Verfolgern fehlt jegliche Spur. Sie müssen aufgegeben haben. \nAm Flussufer legst du dich erst mal auf den Boden und versuchst wieder zu Atem zu kommen. \n")
                                    game=False
                                    chap4_0()
                                    break
                                else:
                                    print("Du schaffst es leider nicht an den Wildschweinen vorbei... \nDu wirst von mehreren Wildschweinen attackiert und gehst zu Boden.\n")        
                                    youdied()
                                    break
                            else: #nein
                                antwort2=""
                                print("Du wirst von mehreren Wildschweinen attackiert und gehst zu Boden.\n")
                                youdied()
                                break   
                    elif antwort== richtungen[3]: #hinten
                            print("Du drehst dich in die Richtung um aus der du gekommen bist. \nZu deiner Überraschung bemerkst du noch mehr Wildschweine die sich aus dieser Richtung um dich versammeln. \nWillst du trotzdem versuchen an ihnen vorbeizurennen? \n")
                            antwort2 = input("Versuchen durch die Schweinegruppe zu rennen? ")
                            print(ja_nein)
                            if antwort2 == ja_nein[1]: #ja
                                print('Du rennst geradeaus auf die Wildschweine zu. \nDumme Idee! \nDie Tiere sehen das als Angriff und tun alles um ihren Nachwuchs zu beschützen. \nDu wirst von mehreren Seiten aus attackiert und gehst zu Boden.\n')
                                youdied()
                                break
                            else: #nein
                                print("Anstatt auf die Tiere zuzulaufen nimmst du vernünftigerweise einen anderen Weg ohne Wildschweine vor dir. \nDu bist eigentlich schon längst an deinen körperlichen Grenzen aber das Adrenalin lässt dich weiter rennen bis du irgendwann auf einen kleinen Fluss stößt. \nDu siehst keine andere Möglichkeit mehr und springst hinein. \nDie Strömung treibt dich ein ganzes Stück mit aber du schaffst es trotzdem ans andere Ufer zu gelangen. \nVon deinen Verfolgern fehlt jegliche Spur. Sie müssen aufgegeben haben. \nAm Flussufer legst du dich erst mal auf den Boden und versuchst wieder zu Atem zu kommen.")       
                                game=False
                                chap4_0()
                                break
                    else:
                        print("Ich verstehe nicht was du mir sagen willst...\n")
                        antwort=""
                            
                            