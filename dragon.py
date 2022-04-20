class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):

        self.health -= damage
        if self.health <0:
            self.health = 0
    def talk(self):
        print(self.name, 'health', self.health, 'Hit me!')

    def final_cry(self):
        print(self.name, 'Dead!')

def main():
    enemy = Dragon('Smog')
    enemy_list = [Dragon('Smog'), Dragon('Hudra')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive():
            enemy_list.pop(0)
            enemy.final_cry()
        if not enemy_list:
            finish = True
    print('You win!')




main()