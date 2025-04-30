from Users import Users

class Rider(Users):
    def __init__(self,user_id, email,name):
        super().__init__(user_id,email,name)
        self.ride_history=[]