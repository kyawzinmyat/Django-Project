class Empty:
	def __init__(self,register_class):
			self.register = register_class
			
	def register(self):
			print("Invalid")
			return self.register.get()
			
class Validate:
	def __init__(self,register_class):
		self.register = register_class
	
class Existed:
	def __init__(self,register_class):
		self.register = register_class
		