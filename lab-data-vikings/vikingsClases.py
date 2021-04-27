
# Soldier
class Soldier:
    def __init__(self,health, strength):
        self.health = health
        self.strength = strength 
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0 :
            return ('{name} has received {damage} points of damage')
        else:
            return ('{name} has died in act of combat')
    
    def battleCry(self):
        return ('Odin Owns you All!')

# Saxon
class Saxon:
    class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return ('A Saxon has received {damage} points of damage')
        else:
            return ('A Saxon has died in combat')

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self):
        self.saxonArmy.append(sak)
        
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
    
     #falta
