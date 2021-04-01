class Vendor:
      def __init__(self, inventory=[]):
            self.inventory = inventory
          
            
            
            

      def add(self, item):
            self.inventory.append(item)
            return self.inventory[-1]

      def remove(self, item):
            if item in self.inventory:
                  self.inventory.remove(item)
                  return item
            return False

