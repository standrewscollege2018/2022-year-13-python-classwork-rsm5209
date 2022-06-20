''' This program demonstrates how classes and object orientation work '''

class Enemy:
    ''' The enemy objects are what the player fights in the game ''' 
    
    def __init__(self, name, health):
        ''' The init function is called when a new object is instantiated it begins and ends with two underscores'''
        # Set the name
        self._name = name
        
        # Set the health
        self._health = health
        
        # Scare the world with a villanous laugh!
        print("Mwa ha ha ha")
   
   
    def get_name(self):
        ''' this function returns the name of the enemy object '''
        
        return self._name
    
    def get_health(self):
        ''' This is a getter function that returns the health of the enemy '''
        
        return self._health
    
    def attacked(self, damage):
        ''' This function is called when the enemy is attacked. The damage value is deducted from the _health value '''
        
        self._health -= damage 
        if self._health <= 0:
            print(f"{self._name} is dead")
        else:
            print(f"Ouch, {self._name} is hurt")

# Create a new enemy object 
enemy1 = Enemy("Gru", 20)
enemy2 = Enemy("Bob", 12)
enemy1.attacked(2)
print (f"{enemy1.get_name()} has {enemy1.get_health()} health left")
print (f"{enemy2.get_name()} has {enemy2.get_health()} health left")
enemy1.attacked(2)