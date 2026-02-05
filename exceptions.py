# Age error
class InvalidAgeError(Exception):
    def __init__(self, message="Age can't smaller than 0"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'ERROR: {self.message}'
    


    
    

