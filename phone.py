from item import Item 

class Phone(Item):
    
    def __init__(self, name:str, price:float, quantity:int, broken_phones = 0):
        # Call to super
        super().__init__(
            name, price, quantity
        )


        assert broken_phones >= 0, f'Broken phones {broken_phones} is not >= 0'

        self.broken_phones = broken_phones