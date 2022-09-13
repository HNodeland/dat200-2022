#Hanois tårn. Målet er å kunne løse puslespillet med en rekursiv algoritme.
#Denne varianten skal skrive ut tilstanden til alle 3 tårnene etter hvert flytt.
#

class Tower:
    def __init__(self, n):
        self.leftTower = []
        for i in range(n):
            self.leftTower.append(i+1)
        self.middleTower = []
        self.rightTower = []

    def printTowers(self):
        print(self.leftTower)
        print(self.middleTower)
        print(self.rightTower)

if __name__ == "__main__":
    t = Tower(3)
    t.printTowers()

