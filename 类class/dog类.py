class Dog():
    def __init__(self,name,age):        #Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self
        self.name = name                #name属性
        self.age  = age
        self.cost = 0                   #给cost属性指定默认值    

    def sit(self):                          #只有一个形参self
        print(self.name.title() +" is sitting now")
    def roll_over(self):
        print(self.name.title() +" rolls over")
    def all_cost(self):
        print(self.name.title() +" has cost " + str(self.cost) +" yuan since last year." )
    def update_money(self,vari_money):
        if vari_money >= self.cost:
            self.cost = vari_money                     #给cost属性变量值  
        else:
            print("you cannot roll back ")
    def add_money(self,money):
        self.cost += money



if __name__ == "__main__":
    my_dog = Dog("white",6)                  #根据类创建实例
    your_dog = Dog("black",5)
    print("My dog's name is " + my_dog.name)

    my_dog.sit()
    my_dog.all_cost()             #White has cost 0 yuan since last year.

    #修改属性值
    my_dog.update_money(15)
    my_dog.all_cost()             #White has cost 15 yuan since last year.
    my_dog.add_money(10)
    my_dog.all_cost()             #White has cost 25 yuan since last year.


