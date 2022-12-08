class Space(object):
    def __init__(self,x,y,value =-1):
        self.x = x
        self.y = y
        self.value = value
    def set_coordinates(self,x,y):
        self.x = x
        self.y = y
    def set_value(self,value):
        self.value = value
    def return_value(self):
        return self.value
    def __str__(self):
        return f"Space @{self.x},{self.y} with value {self.value}"
    
