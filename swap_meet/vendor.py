#wave1 first two tests
class Vendor:
      def __init__(self, inventory=None):
            if inventory ==None:
                  self.inventory =[]
            else:
                  self.inventory = inventory
      #wave1 remaining tests
      def add(self, item):
            self.inventory.append(item)
            return item
      
      def remove(self, item):
            if item in self.inventory:
                  self.inventory.remove(item)
                  return item
            return False
      #wave2
      def get_by_category(self,category=""):
            new_list =[]
            for each_item in self.inventory:
                  if  each_item.category == category:
                        new_list.append(each_item)
                  
            return new_list
      #wave3 last 4 test
      def swap_items(self, friend_list, item_1, item_2):
            if item_1 in self.inventory and item_2 in friend_list.inventory:
                  self.inventory.remove(item_1)
                  friend_list.inventory.append(item_1)
                  friend_list.inventory.remove(item_2)
                  self.inventory.append(item_2)
                  return True
            return False
      #wave4
      def swap_first_item(self,friend_list):
            
            if len(self.inventory)> 0 and len(friend_list.inventory) > 0:
                  item_1=self.inventory[0]
                  item_2=friend_list.inventory[0]
                  self.inventory.remove(item_1)
                  self.inventory.insert(0,item_2)
                  friend_list.inventory.remove(item_2)
                  friend_list.inventory.insert(0,item_1)
                  return True
            return False      
      
      def get_best_by_category(self,best_category):
            items_in_category = self.get_by_category(best_category)
            if len(items_in_category)==0:
                  return None
            max_value = 0
            most_condition_item =""
            for item in items_in_category:
                  if item.condition> max_value:
                        max_value=item.condition
                        most_condition_item=item
            return most_condition_item
                  

      def swap_best_by_category(self,other,my_priority,their_priority):
            tai_list_by_category =self.get_by_category(their_priority)
            jess_list_by_category = other.get_by_category(my_priority)

            if len(tai_list_by_category)!=0 and len(jess_list_by_category)!=0:
                  tai_item_to_swap=self.get_best_by_category(their_priority)
                  jess_item_to_swap = other.get_best_by_category(my_priority)
                  self.swap_items(other,tai_item_to_swap,jess_item_to_swap)
                  return True

            return False
                  

      

