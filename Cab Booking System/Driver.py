from Users import Users

class Driver(Users):
    def __init__(self,user_id,email, name):
        super().__init__(user_id,email,name)
        self.is_available= True
        self.ride_history=[]


    