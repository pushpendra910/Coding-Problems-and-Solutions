class Laptop:
    def __init__(self,name,model,price):
        self.Name=name
        self.Model=model
        self.Price=price 
        pass

p=Laptop("HP","Gaming",78)
print(p.Name)
print(p.Model)
print(p.Price)