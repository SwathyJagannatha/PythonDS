# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method using 
# super() 
class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		# Calling the parent's class 
		# method 
		super().show() 
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show()