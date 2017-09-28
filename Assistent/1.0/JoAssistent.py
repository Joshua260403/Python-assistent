import time
import random
import sys

with open('BotNaamBestand', 'r+') as naambot:
    botnaam = naambot.read()

with open('UserNaamBestand', 'r+') as naamuser:
    usernaam = naamuser.read()

with open('WelkomBestand', 'r+') as welkom:
    welkombericht = welkom.read()

screen = 'start'

if botnaam == "":
    print('Geen data gevonden, automatische reset naar standaard')
    screen = "default"
elif usernaam == "":
    print('Geen data gevonden, automatische reset naar standaard')
    screen = "default"
elif welkombericht == "":
    print('Geen data gevonden, automatische reset naar standaard')
    screen = "default"

while 2 > 1:
    
    if screen == 'start':
        print("\n" + botnaam + " Opstarten\n")
        time.sleep(1)
        print(welkombericht)
        time.sleep(0.5)
        screen = 'home'
    
    if screen == 'home':
        print("\nWat wil je doen?")
        keuze = input("\n\
Kies 0 om " + botnaam + " af te sluiten\n\
Kies 1 om naar de instellingen te gaan\n\
Kies 2 om de tijd en datum te zien\n\
\n\
")
        if keuze == '0':
            time.sleep(0.5)
            print("\nTot ziens " + usernaam + "\n")
            time.sleep(1)
            sys.exit()
        elif keuze == '1':
            screen = 'settings'
        elif keuze == '2':
            screen = 'tijd'
    
    
    if screen == 'settings':
        print("\nWat wil je veranderen?")
        keuze = input("\n\
Kies 0 om alles terug te draaien naar de standaard instellingen\n\
Kies 1 om namen te veranderen\n\
Kies 2 om het Welkomst bericht te wijzigen\n\
\n\
")
        if keuze == '0':
            screen = 'default'
        elif keuze == '1':
            screen = 'namen'
        elif keuze == '2':
            screen = 'welkomedit'
    
    
    if screen == 'default':
        with open('BotNaamBestand', 'r+') as naambot:
            naambot.truncate()
            naambot.write('JoAssistent')
        botnaam = 'JoAssistent'
        with open('UserNaamBestand', 'r+') as naamuser:
            naamuser.truncate()
            naamuser.write('Assistentua')
        usernaam = 'Assistentua'
        with open('WelkomBestand', 'r+') as welkom:
            welkom.truncate()
            welkom.write('Hallo wereld!')
        welkombericht = 'Hello world!'
        screen = 'start'

    if screen == 'tijd':
        print("\nVertaling van de datum is nog niet beschikbaar.")
        datum = time.strftime("%A %d %B %Y %H:%M")
        print(datum + "\n")
        time.sleep(1)
        screen = 'home'

    if screen == 'namen':
        nieuweusernaam = input("\nGeef een nieuwe naam op voor gebruiker: " + usernaam + "\n")
        usernaam = nieuweusernaam
        with open('UserNaamBestand', 'r+') as naamuser:
            naambot.truncate()
            naamuser.write(nieuweusernaam)

        nieuwebotnaam = input("\nGeef een nieuwe naam op voor bot: " + botnaam + "\n")
        botnaam = nieuwebotnaam
        with open('BotNaamBestand', 'r+') as naambot:
            naauser.truncate()
            naambot.write('nieuwebotnaam')
        screen = 'home'

    if screen == 'welkomedit':
        nieuwwelkom = input("\nGeef een nieuw welkomstbericht op: ")
        with open('WelkomBestand', 'r+') as welkom:
            welkom.truncate()
            welkom.write(nieuwwelkom)
        welkombericht = nieuwwelkom
        screen = 'home'
