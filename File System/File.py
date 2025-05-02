from Entity import Entity

class File(Entity):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.content=""
    
    def read(self):
        return self.content
    
    def write(self,data):
        self.content= data

    def append(self,data):
        self.content+=data
    
    def get_size(self):
        return len(self.content)
