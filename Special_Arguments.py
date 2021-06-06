# Python program to illustrate   
# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('My Name is Vinit','Bye Bye ') 

def myFun1(**kwargs):  
    for key,value in kwargs.items():  
        print ("My {} is {}".format(key,value)) 
    
myFun('My Name is Vinit','Bye Bye') 
myFun1(name="vinit")


