class Entity:
    def __init__(self, name, parent=None):
        self.name= name
        self.parent= parent
    
    def get_path(self):
        path=[]
        current=self
        while current:
            path.append(current.name)
            current=current.parent
        return "/"+"/" .join(reversed(path))