#Method means function that perform operation on data
'''
Types of Methods:
    1.instance method
    2.class method 
    3.static method
'''

'''
1.instance method:
        it is performed operations on instance attribute
        first parameter of instance method is self
        we can call instance method by using object reference
        we can access class attribute also by using classname/object reference
    syntax-
        class Xyz:
                def __init__(self):
                    self.ia=v1
            
                def m1(self):   #instance method
                    result=ia*2   
        x=Xyz()
        x.m1()
'''
class Student:
    course="Python"
    trainer="Vaibhav Patil"
    def __init__(self,r,nm,a):
        self.roll=r
        self.name=nm
        self.age=a
        self.marks={}

    def show_details(self):
        details=f'''
                Roll  : {self.roll}
                Name  :  {self.name}
                Age   :  {self.age}
                Course : {Student.course}
                Trainer : {Student.trainer}

            '''
        print(details)
        return "hello"

    def add_marks(self,testname,mk):
        self.marks[testname]=mk
        return self.marks

    def cal_percentage(self):
        obt=0
        for mk in self.marks.values():
            obt=obt+mk
        total=100*len(self.marks)
        per=obt/total*100
        return per

    def show_result(self):
        p=self.cal_percentage()
        if p>40:
            return "Pass"
        else:
            return "Fail"



s1=Student(1,"sanika",20)
s2=Student(2,"chaitrali",21)
print(s1.show_details())
print(s1.add_marks("test1",45))
print(s1.add_marks("test2",65))
print(s2.add_marks("test1",85))
print(s1.cal_percentage())
print(s1.show_result())









