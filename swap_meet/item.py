
class Item:
      def __init__(self, category="",condition=0):
            self.category = category
            self.condition = condition

      def __str__(self):
            return "Hello World!"

      def condition_description(self):
            # return ""
            condition_description = ""
            # for self.condition in range(5):
                  # print(self.condition)
            
            if self.condition >=5:
                  condition_description ="A"
            elif self.condition >=4:
                  condition_description ="B"
            elif self.condition >=3: 
                  condition_description ="C"
            elif self.condition >=2:
                  condition_description ="D"
            elif self.condition >=1:
                  condition_description ="E"
            else:
                  condition_description ="F"

            return condition_description


                  


