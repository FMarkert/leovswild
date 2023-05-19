from actions import *



def chap2_2():
    import random
    from kap3_0 import chap3_0
    antwort=""
    antwort2=""
    global lifepoints
    
    game=True

    while game==True:

        if lifepoints==[]:
                    game=False
                    break


        while antwort not in aktionen:
            print(aktionen)
            antwort = input("Was machst du? ")
            if antwort == aktionen[0]: #umsehen
                print_slowly("\nEs bleibt keine Zeit sich umzusehen...")
                antwort =""
            elif antwort == aktionen[1]: #aufheben
                print_slowly('\nDu merkst wie das Adrenalin ein deinen Kopf schießt. \nDas ist nicht deine erste Prügelei und in deiner Familie wird eine Kampftechnik von Generation zu Generation weitergegeben, mit der sich auch deutlich größere und stärke Gegner in die Knie zwingen lassen. \nDu hast dir eigentlich geschworen, diese Technik nicht mehr einzusetzen aber diese brenzlige Situation lässt dir keine andere Wahl. \nDer Typ holt aus um dir einen Schlag ins Gesicht zu verpassen aber du weichst gekonnt aus, schaffst es deinen Arm um seinen Hals zu legen und wendest deine Spezialtechnik ein: den Schwitzkasten des Todes. \nDein Gegner hat keine Chance sich zu befreien, wird ganz blau im Gesicht und sinkt in sich auf seine Knie zusammen. \nDer Kampf scheint für dich entschieden zu sein als auf einmal Ana de Armas mit den dicken Backen von hinten auf dich zukommt und dir einen großen Stein über den Kopf zieht. \nDu spürst erst unglaubliche Schmerzen, dann wird dir schwarz vor Augen und du fällst in Ohnmacht.\n') 
                antwort=""
                youdied()
                break
            elif antwort == aktionen[2]: #reden
                print_slowly('\n"Beruhig dich! Das ist ein Missverständnis!“ versuchst zu erklären aber der Typ lässt nicht mit sich reden. \nEr holt zum Schlag aus aber du schaffst es auszuweichen. \nJetzt wäre die perfekte Gelegenheit sich zu wehren. Möchtest du zuschlagen?\n')
                print(ja_nein)
                antwort2 = input("Zuschlagen? ")
                if antwort2 == ja_nein[1]:
                    chance = random.uniform(0,1)
                    if chance >= 0.5:
                        print_slowly("\nDu verpasst dem Mann mit deiner Pranke einen Schlag ins Gesicht, der sich gewaschen hat. \nDer Schlag hat so gut gesessen, dass der Kerl sofort zu Boden geht. \nDie junge Frau kreischt laut und die ganze Situation wird dir langsam viel zu wild. \nDu schaust, dass du schnell Land gewinnst. \nSollte das ganze irgendwelche rechtlichen Konsequenzen haben kannst du dich auf Notwehr berufen. \nDu rennst schnell an ihnen vorbei. \nDie Situation war irgendwie super weird und du hast absolut keine Lust mehr auf Stress. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.\n")
                        game=False
                        chap3_0()
                        break
                    else:
                        print_slowly('\nDein Schlag ging leider auch daneben. Dafür sitzt der nächste Schlag deines Gegners umso besser: \nEr erwischt dich mitten im Gesicht und du spürst noch ein schmerzhaftes Knacken als deine Nase bricht. \nDann wird dir schwarz vor Augen und du fällst in Ohnmacht.\n')
                        antwort=""
                        youdied()
                        break                              
                else:
                    print_slowly("\nDu stehst rum und machst nichts. Der Typ schlägt dir ins Gesicht und du gehst K.O...\n")
                    antwort=""
                    youdied()
                    break

            elif antwort == aktionen[3]: #fliehen
                print_slowly('\nDer Typ holt zum Schlag aus aber du schaffst es erfolgreich auszuweichen. \nDu gibst auf einmal richtig Gas und rennst an den beiden vorbei. \nDer Typ verfolgt dich noch einige Meter aber kommt deutlich schneller außer Atem als du. \nAls die beiden außer Sichtweite sind wirst du langsamer. Das Adrenalin hat dich lange rennen lassen und du bist froh, dass du dich nicht auf die Prügelei eingelassen hast. \n„Ich bin zu hübsch für den Knast“ denkst du dir stolz. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.')
                game=False
                chap3_0()
                break
            elif antwort == aktionen[4]: #nichts
                print_slowly("\nDu stehst rum und machst nichts. Der Typ schlägt dir ins Gesicht und du gehst K.O...\n")
                antwort=""
                youdied()
                break
            else:
                print_slowly("\nIch verstehe nicht was du mir sagen willst...\n")
        
      