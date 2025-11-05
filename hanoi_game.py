from hanoi_tower import Tower

class Hanoi:
    
    def __init__(self, num_disks:int, target:int, num_towers:int):
        self._num_disks = int(num_disks)
        self._target = int(target)
        self._num_towers = int(num_towers)
        self._towers = [Tower(num_disks, 0)]
        for tower in range(1, self._num_towers):
            self._towers.append(str(Tower(num_disks, num_disks)))
        
    def __str__(self):
        string = ""
        count = 0
        for tower in range(self._num_disks + 1):
            for row in self._towers:
                string += str(row).split()[tower] + " "
            string += "\n"
        return string


print(Hanoi(3, 3, 3)) #Test
