def chap0():

    from kap1 import chap1
    from actions import print_slowly

    print("\n\n\n")

    with open("banner.txt","r") as f:
        banner = f.read()
        print(banner)

    print("\n\n\n")
    print_slowly("\nPROLOG\n")
    print_slowly("\nWillkommen bei Leo vs. Wild, einem actiongeladenen Text-Adventure aus dem Hause Gelände Productions.\nBei einem Text-Adventure handelt es sich um ein rein textbasiertes Abenteuer.\n\nJa, du hast richtig gelesen. Statt schicker High-End-Grafik und atemberaubender Musik erwartet dich Text … viel Text. \nEs ist ein bisschen wie „Pen & Paper“, nur dass der Computer ein stummer Spielleiter ist, der dich in Form textbasierter Nachrichten auf ein Abenteuer schickt.\n")
    print_slowly("\nDieses Spiel erwartet Eingaben vom Spieler und reagiert dann darauf.\nDem Spieler stehen mehrere Handlungen zur Auswahl, die er durch die Wahl eines geeigneten Wortes aktivieren kann. \nFolgende Eingaben und die damit verbundenen Handlungen stehen dir in diesem Spiel je nach Situation zur Verfügung:\n\n")



    print_slowly("\nja, nein, links, rechts, vorne, hinten, umsehen, aufheben, reden, fliehen, nichts\n\n")

    print_slowly("\nBitte achte darauf die Eingaben kleingeschrieben und wie oben aufgeführt einzugeben, da das Spiel sonst nicht versteht was du von ihm willst.\n")

    print_slowly("\nAber genug zu den Regeln... Wer braucht die schon? Verrate mir lieber deinen Namem!\n")

    spieler = input("Mein Name lautet: ")

    print_slowly(f"\nHallo {spieler}, schön dich kennenzulernen!\n\n")

    print_slowly("\nNun kommen wir zu deiner Charakterklasse: \nWelche Klasse würdest du gerne spielen?\n\nZur Auswahl stehen Paladin, Magier, Schurke, Bogenschütze, Barbar, Kleriker, Samurai\n\n")

    klasse = input("Ich wähle als meine Charakterklasse: ")

    print_slowly(f"\nOha! Du willst also ein {klasse} sein... Eine sehr gute Wahl!\n")

    print_slowly(f"\nUnd mit welcher Waffe soll dein {klasse} das Spiel beginnen? \n\nDu hast die Wahl zwischen Schwert und Schild, einem Dolch, einem Kurzbogen, einer Axt, einem Zauberstab oder einem Katana\n")

    waffe = input("Ich entscheide mich hierfür: ")

    print_slowly(f"\nDu bist also {spieler} und möchtest das Spiel als {klasse} mit {waffe} beginnen.\n\nGaaaaaaaanz großes Sorry an dieser Stelle aber daraus wird nichts....\n\n")

    print_slowly("\n\nDu schlüpfst stattdessen in die Rolle von Leo, ein kräftiger Mann aus Russland mit einem Herzen aus Gold.\nUnd dein Abenteuer beginnt genau hier:\n\n")

    chap1()
