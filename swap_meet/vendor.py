class Vendor:
      def __init__(self, inventory=set()):
            self.inventory = inventory
          
            
            
            

      def add(self, item):
            self.inventory.add(item)
            return item

      def remove(self, item):
            if item in self.inventory:
                  self.inventory.remove(item)
                  return item
            return False

      def get_by_category(self,category=""):
            new_list =[]
            for each_item in self.inventory:
                  if  each_item.category == category:
                        new_list.append(each_item)
                  
            return new_list

           
      

