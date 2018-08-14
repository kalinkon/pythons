class Car:

    engine_power = 740

    def __init__(self, owner_name, color):
        self.color = color
        self.owner_name = owner_name


    def change_engine_power(self,new_power):
        self.engine_power = new_power
