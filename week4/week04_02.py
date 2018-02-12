class Value:
    def __get__(self, obj, obj_type):
        return self.value
        
    def __set__(self, obj, value):
        self.value = value - value * obj.commission
        
    def __delete__(self, obj):
        pass
