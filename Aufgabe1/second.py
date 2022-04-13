#from threading import Thread
import heapq
import time
import random
"""
5 - Tupel
(Ereigniszeipunkt,Ereignispriorität,Ereignisnummer,Ereignisfunktion,Args)

"""
# Globale Variblen
Ereignisnummer = 0  #
GlobalTime = 0      # in sec
present = []

# Prio:  1-Verlassen , 2-Beginn, 3-Ankunft


class EventList():
    def __init__(self):
        self.Time = 0
        self.EventList = []
        self.Ereignisnummer = Ereignisnummer
        self.size = 0

    def pop(self):
        e = heapq.heappop(self.EventList)
        self.size -= 1
        # return e

    def push(self, anEvent):
        heapq.heappush(self.EventList, anEvent)
        self.size += 1

    def start(self):
        T1 = Kunde(1)
        T1_Event = T1.begin_einkauf()
        present.append(T1)
        self.push(T1_Event)
        print("Pushed first")

        T2 = Kunde(2)
        T2.timer = 1
        T2_Event = T2.begin_einkauf()
        present.append(T2)
        self.push(T2_Event)
        print("Pushed second")

        while self.size != 0:

            for k in present:
                print(k.timer)
                for e in k.KundenListe:
                    # print(k.KundenListe)
                    if e in walkTime_T1:

                        x = walkTime_T1.get(e, None)
                        k.timer += x
                        print(k.timer)
                        k.ankunft_station()
                    print(k.KundenListe)
                    print(e)

                    # print(k.KundenListe)
            exit()


ourList = EventList()
# Event(1,2,3,4,5)
"""
Prioritäten 1. Verlassen
            2. Beginn
            3. Ankunft
"""


class Event():
    def __init__(self,
                 Ereigniszeitpunkt,
                 Ereignispriorität,
                 Ereignisnummer,
                 Ereignisfunktion,
                 Args):
        self.Ereigniszeitpunkt = Ereigniszeitpunkt
        self.Ereignispriorität = Ereignispriorität
        self.Ereignisnummer = Ereignisnummer
        self.Ereignisfunktion = Ereignisfunktion
        self.Args = Args

    def __repr__(self):
        print(
            f' Event = {self.Ereigniszeitpunkt}, {self.Ereignispriorität}, {self.Ereignisnummer} ,{self.Ereignisfunktion}, {self.Args} \n')

    def __lt__(self, other):
        self.Ereigniszeitpunkt < other.Ereigniszeitpunkt


class Station():
    def __init__(self, Typ):
        self.Typ = Typ
        self.Priority = 2
        self.Kapazität = 10
        self.WarteSchlange = []
        self.used = False

        if Typ == "Kasse":
            self.Bediendauer = 5
        elif Typ == "Bäcker":
            self.Bediendauer = 10
        elif Typ == "Wurst":
            self.Bediendauer = 30
        elif Typ == "Käse":
            self.Bediendauer = 60
        else:
            print(f'/n ooh noo /n')

        print(id(self))

    def anstellen(self, Kunde):
        print(id(self))
        print(f' kunde in warteschlange {Kunde}')
        self.WarteSchlange.append(Kunde)
        # self.fertig(Kunde)

    def fertig(Kunde):
        pass


Bäcker = Station("Bäcker")
Wurst = Station("Wurst")
Käse = Station("Käse")
Kasse = Station("Kasse")

bucket = {"Bäcker": Bäcker, "Wurst": Wurst, "Käse": Käse, "Kasse": Kasse}
walkTime_T1 = {"Bäcker": 10, "Wurst": 30, "Käse": 45, "Kasse": 60}
walkTime_T2 = {"Wurst": 30, "Kasse": 30, "Bäcker": 20}
"""
3 - Tupel 

Wartezeit, Wegzeit, noch zu besuchende Stationen

"""
# , WarteZeit, Strecke, Anzahl


class Kunde():
    def __init__(self, Typ):
        if Typ == 1:
            self.KundenListe = ["Bäcker", "Wurst", "Käse", "Kasse"]
        elif Typ == 2:
            self.KundenListe = ["Wurst", "Kasse", "Bäcker"]
        self.timer = 0

    def begin_einkauf(self):
        first = Event(
            Ereigniszeitpunkt=GlobalTime,
            Ereignispriorität=2,
            Ereignisnummer=Ereignisnummer,
            Ereignisfunktion=self.ankunft_station,
            Args=self.KundenListe)
        print(f'{self} entered the supermarket')
        for e in self.KundenListe:
            pass
        return first

    def ankunft_station(self):

        toVisit = self.KundenListe[0]
        stat = bucket[toVisit]
        if not stat.used:
            self.timer += stat.Bediendauer
            print(self.timer)
            stat.used = True
            print(
                f'Kunde ist bei {bucket[toVisit].Typ} + {bucket[toVisit].Bediendauer}')
            self.KundenListe.remove(toVisit)
        else:
            Station.anstellen(toVisit, self)
            print(f' {self} hat sich angestellt\n')
            self.KundenListe.remove(toVisit)
        second = Event(Ereigniszeitpunkt=GlobalTime,
                       Ereignispriorität=3,
                       Ereignisnummer=Ereignisnummer,
                       Ereignisfunktion=self.ankunft_station,
                       Args=self.KundenListe)
        ourList.push(second)
        print(f'pushed ankunftEvent to Eventlist \n')

    def verlassen_station(self):
        pass


def main():

    ourList.start()
    #print(ourList.EventList[0], ourList.EventList[1])
    #print(f'presentList -> {present}')
    # print(ourList)


main()
