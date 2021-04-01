class Vendor:
      def __init__(self, inventory=[]):
            self.inventory = inventory
          
      def add(self, item):
            self.inventory.append(item)
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

      def swap_items(self, friend_list, item_1, item_2):
            if item_1 in self.inventory and item_2 in friend_list.inventory:
                  self.inventory.remove(item_1)
                  friend_list.append(item_1)
                  friend_list.remove(item_2)
                  self.inventory.append(item_2)
                  return True
            return False

                  
            
    

           
      

