#lottery_player = {
#    'name': 'sam',
#    'numbers': (12, 45, 67, 88)  #values can be list, sets, tuples, dicts
#}
#print(lottery_player['name'])
#print(len(lottery_player['numbers']))
#print(sum(lottery_player['numbers']))
#
#
#
#
#
#
#
#
#class LotteryPlayer:
#    def __init__(self):
#        self.name = "Sam"
#        self.numbers = (5, 6, 8, 3, 1, 20)
#        
#    def total(self):
#        return sum(self.numbers)
#        
#        
#player = LotteryPlayer()
##player.name = "Josh"
##player.numbers = [(2, 54, 77, 88), {22, 33, 44, 55}]
#print(player.name)
#print(player.numbers)
#
#print(player.total())
#print(sum(player.numbers))
#
#
#
#
#
#player_one = LotteryPlayer()
#player_two = LotteryPlayer()
#
##player_one.name = 'sam'
#
#print(player_one == player_two) #false, two different instances
#print(player_one.name == player_two.name) #true till you define name
#
#
#
#
#
#
#
#
#class LotteryPlayer:
#    def __init__(self, name, numbers):
#        self.name = name
#        self.numbers = numbers
#        
#    def total(self):
#        return sum(self.numbers)
#    
#    
#player_one = LotteryPlayer('Sam', (22, 33, 44, 55, 66))
#player_two = LotteryPlayer('Tom', (33, 44, 55, 66, 77, 90))
#
#print(player_one.name)
#print(player_two.name)
#print(player_one.numbers)
#print(player_two.numbers)
#print(player_one == player_two) 
#print(player_one.name == player_two.name) 
#
#
#
#
#
#
###
#
#class Student:
#    def __init__(self, name, school):
#        self.name = name
#        self.school = school
#        self.marks = []
#        
#    def marks_avg(self):
#        total = sum(self.marks)
#        count = len(self.marks)
#        return(total / count)
#    
#    @staticmethod
#    def go_to_school(): #since we don't need to pass self with this, but it would do it by default, we need staticmethod decorator
#        print('i am going to school')
#        
#    @classmethod
#    def who(cls):
#        print('i am {}'.format(cls))
#        
#        
##Use @classmethod when you need access to the class, but not an instance;
##
##Use @staticmethod when you want to put a method inside a class because it makes sense logically for it to be there, but you don't need access to the class or the instance.
#        
#        
#        
#anna = Student('Anna', 'MIT')
#anna.marks = [22, 33, 44]
#anna.marks.append(69)
#print(anna.marks)
#print(anna.marks_avg())
#anna.go_to_school()
#anna.who()
#
#
#
###
#
#
#
#class Store:
#    def __init__(self, name):
#        self.name = name # You'll need 'name' as an argument to this method.
#        self.items = [] # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
#    
#    def add_item(self, name, price):
#        item_dict = {'name': name, 'price': price}# Create a dictionary with keys name and price, and append that to self.items.
#        self.items.append(item_dict)
#
#    def stock_price(self):
#        # Add together all item prices in self.items and return the total.
##        naive
##        total = 0
##        for item in self.items:
##            total += item['price']
##        return total
#    
#        return sum([i['price'] for i in self.items])
#    
#    
#    
#store1 = Store('Walgreens')
#store1.add_item('apple', 23)
#print(store1.stock_price())
#    
#    
#    
#    
#    
#    
    
###

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        
        return cls(store.name + ' - franchise') #cls is a ref to the class which is Store, so they are interchangeable here, see below
    
#        return Store(store.name + ' - franchise')   - - same thing as above

#        return cls("{} - franchise".format(store.name)) - - yet another way

#        new_store = Store(store.name + " - franchise")   - - -also valid
#        return new_store
    
    


    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price())
    
    

    
    
    
    
    

    