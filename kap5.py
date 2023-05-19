from actions import *

def chap5():
    print_slowly("\nKAPITEL 5 - EPILOG\n\n")
    antwort=""

    print_slowly('\nAlles bisher hat sich wie ein total verrückter Actionfilm angefühlt. \nJetzt ist es still. \nVor dir liegt der Kadaver eines riesigen Wildschweins. \nDu wischst dir Blut aus dem Gesicht, von dem du nicht weißt ob es dein eigenes oder das deines besiegten Widersachers ist. \nDie Schweine um dich herum scheinen dich nicht mehr angreifen zu wollen. \n\nIm Gegenteil: Es scheint fast so, als würden sie ihre Köpfe vor dir senken und einen Ausgang aus dem Kreis, den sie zuvor um dich gebildet haben, freimachen.\n\n') 

    while antwort not in ja_nein:
        print_slowly('\nMöchtest du den Wald jetzt verlassen?\n')
        print(ja_nein)
        antwort=input("Wald verlassen? ")
        if antwort==ja_nein[1]: #ja
            print_slowly('\nDu hast den schmerzhaften Marathon durch den Wald überstanden.\nDeine zerschundenen Beine zittern vor Erschöpfung, als du dich mühsam auf den letzten Meter nach Hause schleppst. \nDer Wald hat deine unschuldige Joggingroutine in einen Albtraum verwandelt, der dich bis in die tiefsten Abgründe seiner Seele geführt hatte. \nDer Blick in deinen Augen zeugt von den schrecklichen Begegnungen, die du mit den Wildschweinen hattest. \nDie Erinnerung an die rasenden Tiere, die ihm hinterherstürmten, brannte sich unauslöschlich in dein Gedächtnis ein. \n\nEs sind nicht nur physische Wunden, die du trägst, sondern auch seelische Narben, die den Schatten der Angst in seinem Inneren hervorriefen. \n\nDie letzten Sonnenstrahlen verschwinden langsam hinter den Baumkronen und die Welt taucht in eine düstere Stille. \nDu spürst den kalten Wind auf deiner Haut, während deine Gedanken immer wieder zu den schlimmen Dingen zurückkehren, die du in diesem Wald erlebt hast. \nEs scheint, als hätten die Schatten der Vergangenheit dich fest im Griff, dich daran erinnernd, wie zerbrechlich das Leben sein kann. \n\nDoch hier stehst du, bereit, dich den Herausforderungen des echten Lebens zu stellen.\n')
            break
        elif antwort==ja_nein[0]: #nein
            print_slowly("\nDie Wildschweine begleiten dich tiefer in den Wald. \nDeine Schritte sind leichter geworden, befreit von der Last der Vergangenheit. \n\nDer Geruch von Moos und Erde umgibt dich und die Stimmen der Vögel begleiten dich auf deinem Weg. \nDie Wildschweine haben dich auserwählt, zum König des Waldes gekrönt, und du hast diese neue Bestimmung mit offenen Armen angenommen. \nIn dieser Welt jenseits der Zivilisation hast du Frieden gefunden, fernab von den Leiden der Menschen. \n\nLegenden erzählen von einem Herrscher, der über die schützenden Bäume wacht, und obwohl niemand dich je wieder gesehen hat, lebst du weiter in den Herzen jener, die den Wald betreten und das Gefühl der Ehrfurcht und Freiheit empfinden, das deine Gegenwart ausstrahlt.\n")
            break
        else:
            print_slowly('Du scheinst in der Sprache der Götter zu sprechen...')
        
    print("\n\n\n\n")
    
    with open("end.txt","r") as f:
        ende = f.read()
        print(ende)  

    