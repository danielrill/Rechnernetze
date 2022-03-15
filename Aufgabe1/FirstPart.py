import threading as th
import heapq as hq
import time


Products = { "Wurst":"Wursttheke", "Steak":"Wursttheke" ,
             "Cheddar": "Käsetheke" , "Gouda":"Käsetheke",
             "Brezel":"Bäcker", "Brötchen":"Bäcker" ,
            }

class Station():
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.waiting = hq()
        self.served = False
        self.limit = 10


    def serve(self, Kunde, Station):
        print("Kunde %s has been served %d", Kunde.name, Kunde.time)
        time.sleep(Station.time)

    def leave(self, Kunde, Station):
        print("Kunde %s finished at %s", Kunde.name, Station.name)
        Kunde.list.remove(Station.name)


    def check(self, Kunde, Station):
        if self.served:
            if self.waiting.length == self.limit:
                self.leave(Kunde)
            else:
                print("Kunde %s added to %s queue", Kunde.name, Station.name)
                self.waiting.heappush(Kunde)
                # bearbeite Kunden Liste
        else:
            self.serve()


def __init__(self, name):
    self.name = None



class Wurst(Station):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.time = 100


class Kasse(Station):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.time = 100


class Käse(Station):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.time = 100


class Bäcker(Station):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.time = 100


class Kunde():
    def __init__(self, name, list):
        pass
        #self.list = hq()
    def visit(Kunde, Station):
        for e in Kunde.list:
            #check()
            pass

class T1_Kunde(Kunde):
    def __init__(self, name, list):
        self.list = ["Bäcker", "Wurst", "Käse"]


class T2_Kunde(Kunde):
    def __init__(self, name, list):
        self.list = ["Wurst", "Bäcker"]
