#wave1 first two tests
class Vendor:
      def __init__(self, inventory = None):
            if inventory is None:
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
                  if each_item.category == category:
                        new_list.append(each_item)
                  
            return new_list
      #wave3 last 4 test
      def swap_items(self, vendor, my_item, their_item):

            if my_item in self.inventory and their_item in vendor.inventory:
                  vendor.add(self.remove(my_item))
                  self.add(vendor.remove(their_item))
                  return True

            return False
      #wave4
      def swap_first_item(self,vendor):
            
            if len(self.inventory)> 0 and len(vendor.inventory) > 0:
                  my_item=self.inventory[0]
                  vendor_item=vendor.inventory[0]
                  # self.inventory[0]=vendor_item
                  # vendor.inventory[0] = my_item
                  # return True
                  return self.swap_items(vendor, my_item, vendor_item)

            return False      
      #wave6 first three tests
      def get_best_by_category(self,best_category):
            items_in_category = self.get_by_category(best_category)
            if len(items_in_category)==0:
                  return None
            max_value = float("-inf") 
            best_condition_item =""
            for item in items_in_category:
                  if item.condition> max_value:
                        max_value=item.condition
                        best_condition_item=item
            return best_condition_item
                  
      #wave6 last three tests
      def swap_best_by_category(self,other,my_priority,their_priority):
            
            my_list_by_category = self.get_best_by_category(their_priority)
            their_list_by_category = other.get_best_by_category(my_priority)

            if my_list_by_category and their_list_by_category:
                  return self.swap_items(other,my_list_by_category,their_list_by_category)

            return False
                  

      

