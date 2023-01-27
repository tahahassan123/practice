class Cake:
    def __init__(self):
        self.ccake = cake()
    def add_type(self, cake_type: str):
        self.ccake.type = cake_type
        return self
    def add_icing(self, icing_type: str):
        self.ccake.icing = icing_type
        return self
    def add_drink(self, drink_type: str):
        self.ccake.drink = drink_type
        return self
    def build(self):
        return self.ccake
class cake:
    def __init__(self):
        self.type = None
        self.icing = None
        self.drink = None
    def __str__(self):
        return f"Cake: {self.type}, Icing: {self.icing}, Drink: {self.drink}"
CakeParty = Cake()
ccake = CakeParty.add_type("Chocolate").add_icing("Vanilla").add_drink("7up").build()
print(ccake)