class Item:
      
      def __init__(self, category="",condition=0):
            self.category = category
            self.condition = condition
      #wave3 first test
      def __str__(self):
            return "Hello World!"
      #wave5  
      def condition_description(self):
            
            if self.condition >=5:
                  return "A"
            elif self.condition >=4:
                  return "B"
            elif self.condition >=3: 
                  return "C"
            elif self.condition >=2:
                  return "D"
            elif self.condition >=1:
                  return "E"
            else:
                  return "F"
            

            


