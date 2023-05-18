from actions import *



def chap2_0():

    global lifepoints
    import random
    from kap2_2 import chap2_2
    from kap3_0 import chap3_0
    print("\nKAPITEL 2\n")
    boyfriend = False #Hilfsvariable für logischen Ablauf
    game = True
    print("Die Sache mit dem Fuchs hat dich schon ein wenig aus der Fassung gebracht \naber du lässt dich von sowas nicht von deinem Ziel abbringen. \nDu joggst den Waldweg weiter entlang.\n")

    print('Der Waldweg macht eine 90 Grad Kurve in einer Lichtung. \nHinter der Kurve, die durch die dichten Büsche und Bäume zuvor nicht einsehbar war, \nbemerkst du wie dir auf einmal eine andere Person mit einem kleinen Hund auf dem Waldweg entgegenkommt.\n ')

    print('Du hast dich heute nicht umsonst für den Wald als Laufstrecke entschieden. \nHeute war so ein Tag an dem du nicht wirklich Lust auf andere Menschen hattest \nund du warst dir sicher an diesem Tag und zu dieser Uhrzeit nicht vielen Leuten im Wald zu begegnen.\n')

    print('Als die unerwünschte fremde Person jedoch genauer zu erkennen ist gefällt dir auf einmal was du vor dir siehst. \nVor dir steht eine junge Frau die dich beim genaueren Hinsehen sofort an die Schauspielerin Ana de Armas erinnert, \nnur das die Frau vor dir deutlich dickere Backen hat als die Hollywood-Schauspielerin. \n')
    print('Du wirst deutlich langsamer und ihr schaut euch gegenseitig an. Dann lächelt sie dich an.\n')
    print('Was machst du?')

    while game==True:
        
        if lifepoints==[]:
                    game=False
                    break

        antwort = ""
      

        while antwort not in aktionen:
            print(aktionen)
            antwort = input("Was machst du? ")
            if antwort == aktionen[0]: #umsehen
                if boyfriend == False:
                    print('Ihr lächelt euch weiter an als es neben euch auf einmal im Gebüsch raschelt. \nAus dem Busch kommt ein mindestens 2 Meter großer breitgebauter Mann südländischer Herkunft im Jogginganzug und mit einer Bauchtasche vor der Brust. \nDer Typ ist offensichtlich ihr Freund oder Mann der im Gebüsch pinkeln war. \nAls er auf die junge Frau zugeht und merkt wie ihr beiden euch anseht wirft er dir einen sehr argwöhnischen Blick zu. \nWie reagierst du?')
                    boyfriend = True
                    antwort=""
                else:
                    print('Der Typ schaut dich immernoch argwöhnisch an...')
                    antwort=""
            elif antwort == aktionen[3]: #fliehen
                if boyfriend==False:
                    print('Du joggst an ihr vorbei. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.\n')
                    game=False
                    chap3_0()
                    antwort =""
                    break
                else:
                    print('Du joggst an ihnen vorbei. Die Situation ist irgendwie super weird und du hast absolut keine Lust auf Stress. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.\n')        
                    game=False
                    antwort=""
                    chap3_0()
                    break
            elif antwort == aktionen[4]: #nichts
                if boyfriend==False: 
                    print('Du joggst an ihr vorbei. Die Situation ist irgendwie super weird und du hast absolut keine Lust auf Stress. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.\n')
                    game=False
                    chap3_0()
                    break
                else:
                    print('Du joggst an ihnen vorbei. Die Situation ist irgendwie super weird und du hast absolut keine Lust auf Stress. \nDu hast dir vorgenommen heute etwas für dich zu tun und keinen Bock auf andere Menschen. \nUm solche Situationen für dein weiteres Workout möglichst zu vermeiden, entscheidest du dich den Rest der Stecke abseits des Waldweges zu gehen. \n„Vertrau mir Leo, du bist geil und kennst dich hier aus im Wald.“ sagst du zu dir als du immer weiter in den Wald hineinläufst.\n')
                    game=False
                    chap3_0()
                    break
            elif antwort == aktionen[1]: #aufheben
                    print('Das ist eindeutig sexuelle Belästigung: \nDu versuchst gerade mitten im Wald eine wildfremde Frau hochzuheben. \nAna de Armas mit dicken Backen gibt ein lautes Kreischen von sich. \n')
                    if boyfriend == True:
                        print('Ihr Freund rennt auf dich zu, reißt dich von ihr weg, du stolperst und fällst rückwärts zu Boden. \nAls du dich wieder aufrichtest hat sich der Mann vor dir aufgestellt und es sieht so aus, als würde er dir gleich eine reinhauen wollen.\n')
                        game=False
                        chap2_2()
                        break
                    else:
                        print('Neben euch aus dem Gebüsch kommt ein mindestens 2 Meter großer breitgebauter Mann südländischer Herkunft im Jogginganzug und mit einer Bauchtasche vor der Brust. \nDer Typ ist offensichtlich ihr Freund oder Mann der im Gebüsch pinkeln war.\n')
                        print('Ihr Freund rennt auf dich zu, reißt dich von ihr weg, du stolperst und fällst rückwärts zu Boden. \nAls du dich wieder aufrichtest hat sich der Mann vor dir aufgestellt und es sieht so aus, als würde er dir gleich eine reinhauen wollen.\n')
                        game=False
                        chap2_2()
                        break 
            elif antwort == aktionen[2]: #reden
                    print('„Hey“ sagst du lächelnd. Die Frau lächelt zurück und sagt ebenfalls „Hey“. \nDie Stimmung ist ziemlich flirty.\n')
                    if boyfriend == True:
                        print('Der Typ neben euch guckt erst das Mädchen an und dann dich. Dann kommt er auf dich zu.')
                        print('„Machst du meine Freundin an, Junge!?!“ schreit er und als der Typ vor dir steht schupst er dich, du stolperst und fällst rückwärts zu Boden. \nAls du dich wieder aufrichtest hat sich der Mann vor dir aufgestellt und es sieht so aus, als würde er dir gleich eine reinhauen wollen.\n')
                        game=False
                        chap2_2()
                        break
                    else:
                        print('Neben euch aus dem Gebüsch kommt ein mindestens 2 Meter großer breitgebauter Mann südländischer Herkunft im Jogginganzug und mit einer Bauchtasche vor der Brust. \nDer Typ ist offensichtlich ihr Freund oder Mann der im Gebüsch pinkeln war.\n')
                        print('„Machst du meine Freundin an, Junge!?!“ schreit er und als der Typ vor dir steht schupst er dich, du stolperst und fällst rückwärts zu Boden. \nAls du dich wieder aufrichtest hat sich der Mann vor dir aufgestellt und es sieht so aus, als würde er dir gleich eine reinhauen wollen.\n')
                        game=False
                        chap2_2()
                        break
            else:
                print('Eingabe nicht verstanden...')
                    




                

                            
        