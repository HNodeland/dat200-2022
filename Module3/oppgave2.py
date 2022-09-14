from tracemalloc import start


class Towers:
    def __init__(self, disks):
        self.disks = disks
        self.towers = [[],[],[]]
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []

    def move(self, startingTower, targetTower):
        self.towers[targetTower].append(self.towers[startingTower][-1])
        self.towers[startingTower].pop()
    
    def solve(towers, n, startingTower, targetTower, placeholderTower):
        if n > 0:
            towers.solve(n-1, startingTower, placeholderTower, targetTower)
            towers.move(startingTower, targetTower)
            towers.printTowers()
            towers.solve(n-1, placeholderTower, targetTower, startingTower)
    
    def printTowers(self):
        print("")
        print(self.towers[0])
        print(self.towers[1])
        print(self.towers[2])


if __name__ == "__main__":
    t = Towers(4)
    t.printTowers()
    t.solve(t.disks, 0, 2, 1)
    
