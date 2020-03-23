class First:
    name ="Chintu"
    def getName(self ,n):
        self.name=n
        print("hello",self.name)
#instances object ->attribute refrencing
#instance = classname()
obj=First()
#obj.name="Pintu"
obj.getName('Pintu')
#ClassName.__methodname__(instance object)
obj1=First()
obj1.name="Pappu"
obj.getName('Papu')
print("Name is ",First.name)
