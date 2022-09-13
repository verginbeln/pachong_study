# 要编写的类是另一个现成类的特殊版本，可使用继承。原有的类称为父类，
# 而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

#区分属性(变量)，方法（def），实例(class)

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
    def tail(self):
        print("Tail is so cute")
    def update_money(self,vari_money):
        if vari_money >= self.cost:
            self.cost = vari_money                     #给cost属性变量值  
        else:
            print("you cannot roll back ")
    def add_money(self,money):
        self.cost += money


class Body():
    #狗的身体
    def __init__(self, body_width=30):  
        self.body_width = body_width 
    def describe_body(self):            
        print("This dog is " +str(self.body_width)+" mmm")
    def good_or_bad_body(self):
        if self.body_width >= 50:
            about = "good"
        else:
            about = "bad"
        print(about)


class Keji_Dog(Dog):
    """子类，柯基"""
    def __init__(self,name,age): 
    # """初始化父类属性"""
       super().__init__(name,age)      #super()是一个特殊函数，帮助Python将父类和子类关联起来
       self.keji_head_length = 50
       self.body = Body()             #将实例用作属性：：创建一个新的Body实例（由于没有指定尺寸，因此为默认值30），并将该实例存储在属性self.body中。
                                      #每当方法__init__()被调用时，都将执行该操作；因此现在每个Keji_Dog实例都包含一个自动创建的Body实例。
    
    def keji_head(self):            #给子类定义属性和方法,,,,,,
        print("This dog is " +str(self.keji_head_length)+" cm")
    def tail(self):                             #也可以重写父类里的方法放在子类里，影响子类
        print("keji doesnot have tail")


if __name__ == "__main__":
    my_keji = Keji_Dog("sissy",15)
    my_keji.keji_head()
    my_keji.body.good_or_bad_body()
