class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    #wave3 first test
    def __str__(self):
            return "Hello World!"

    #wave5  
    def condition_description(self):
        if self.condition >= 5:
            return "Mint"
        elif self.condition >= 4:
            return "Excellent"
        elif self.condition >= 3: 
            return "Great"
        elif self.condition >= 2:
            return "Good"
        elif self.condition >= 1:
            return "Just Ok"
        else:
            return "Poor"
            

            


