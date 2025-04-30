from LRU import LRU
from Node import Node

class LRUDemo:
    @staticmethod
    def run():
        cache = LRU(3)

        cache.put(1, "Value 1")
        cache.put(2, "Value 2")
        cache.put(3, "Value 3")

        print(cache.get(1))  
        print(cache.get(2))  
        cache.put(4, "Value 4")  

        print(cache.get(3))  
        print(cache.get(4))  
        cache.put(2, "Updated Value 2")  

        print(cache.get(1)) 
        print(cache.get(2)) 


if __name__ == "__main__":
    LRUDemo.run()