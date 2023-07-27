class Fridge:
    def __init__(self, items={}):
        if type(items) != type({}):
            raise TypeError ("Fridge requires dict but given a %s" % type(items))
        self.items = items
        return
    
    def __add_multi(self, food_name, quantity):
        if not self.items.__contains__(food_name):
            self.items[food_name] = 0
        
        self.items[food_name] = self.items[food_name] + quantity
        
    def add_one(self, food_name):
        if type(food_name) != type(""):
            raise TypeError ("add_one requires a string, given a %s" % type(food_name))
        else:
            self.__add_multi(food_name,1)
            
        return True
    
    def add_many(self, food_dict):
        if type(food_dict) != type({}):
            raise TypeError ("add_many requires a dictionary, got a %s" % food_dict)
        
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
            
        return
    
    def has(self, food_name, quantity=1):
        return self.has_various({food_name:quantity})
    
    def has_various(self, foods):
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        
        except KeyError:
            return False
        
    def __get_multi(self, food_name, quantity):
        try:
            if not self.has(food_name, quantity):
                return False
            self.items[food_name] = self.items[food_name] - quantity
            
        except KeyError:
            return False
        
        return quantity
    
    def get_one(self, food_name):      
        if type(food_name) != type(""):
            raise TypeError ("get_one requires a string, given a %s" % type(food_name))
        else:
            result = self.__get_multi(food_name,1)
        
        return result
    
    def get_many(self, food_dict):
        
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed
    
    def get_ingredients(self, food):
        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        
        if ingredients != False:
            return ingredients

class Omelet:
    def __init__(self, kind = "cheese"):
        self.set_kind(kind)
        self.mixed = False
        self.cooked = False
        return
    
    def __ingredients__(self):
        return self.needed_ingredients
    
    def get_kind(self):
        return self.kind
    
    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.needed_ingredients = possible_ingredients
            
    def set_new_kind(self, name, ingredients):
        self.kind = name
        self.needed_ingredients = ingredients
        return
    
    def __known_kinds(self, kind):
        if kind == "cheese":
            return {"eggs" : 2, "milk" : 1, "cheese" : 1}
        elif kind == "mushroom":
            return {"eggs" : 2, "milk" : 1, "cheese" : 1, "mushroom" : 2}
        elif kind == "onion":
            return {"eggs" : 2, "milk" : 1, "cheese" : 1, "onion" : 1}
        else:
            return False
        
    def get_ingredients(self, fridge):
        self.from_fridge = fridge.get_ingredients(self)
        
    def mix(self):
        for ingredients in self.from_fridge.keys():
            print("Mixing %d %s for the %s omelet" % (self.from_fridge[ingredients], ingredients, self.kind))
        
        self.mixed = True
        
    def make(self):
        if self.mixed == True:
            print("Cooking the %s Omelet" %self.kind)
            self.cooked = True


class Meal:
    ''' Doc string for Meal Class with setter methods'''
    
    def __init__(self, food="omelet", drink="coffee"):
        self.name = "generic meal"
        self.food = food
        self.drink = drink
        
    def printIt(self, prefix=" "):
        '''Print data nicely..'''
        print(prefix, "A fine", self.name, "with", self.food, "and", self.drink)
        
    def setFood(self, food="omelet"):
        self.food = food
        
    def setDrink(self, drink="coffee"):
        self.drink = drink
        
    def setName(self, name=" "):
        self.name = name
        

class Breakfast(Meal):
    '''Breakfast for the athlete'''
    
    def __init__(self):
        '''Initialize with omelet and coffee'''
        Meal.__init__(self, "omelet", "coffee")
        self.setName("Breakfast")
        
class Lunch(Meal):
    '''Lunch Baby...'''
    
    def __init__(self):
        '''Initialize with sandwich and gin and tonic'''
        Meal.__init__(self, "sandwich", "gin and tonic")
        self.setName("Midday Meal")
        
    #Override setFood()
    
    def setFood(self, food="sandwich"):
        if food != "sandwich" and food != "omelet":
            raise AngryChefException
            Meal.setFood(self, food)
            
class Dinner(Meal):
    '''Dinner gourmet style'''
    
    def __init__(self):
        '''Initialize with steak and merlot'''
        Meal.__init__(self, "steak", "merlot")
        self.setName("Dinner")
        
    #Override setFood()
    
    def printIt(self, prefix= " "):
        print(prefix, "A gourmet", self.name, "with", self.food, "and", self.drink)
               
        
class SensitiveArtistException(Exception):
    pass

class AngryChefException(SensitiveArtistException):
    pass

def test():
    
    '''Test Function'''
    
    print("Module meal test")
    

    
if __name__ == '__main__':
    test()
