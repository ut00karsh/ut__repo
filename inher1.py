if __name__=="__main__":
	
	"""class a:
	

		a1=10
		__b=10
		print __b,"private memeber of a"
		
		def __init__(self,x,y):
			self.x=x
			self.y=y
			print a.__b,"private member of inherited class a"
		
		
			
	class b(a):
		
		c=5
		
		def __init__(self,x,y):
			self.x=x
			self.y=y
			print a.__b,"private member of inherited class a"
		
		
		
	class d(a,b):
		def __init__(self,x,y):
			self.x=x
			self.y=y
			print a.__b,"private member of inherited class a"
		
		super(d,self).__init__()
		
		def sub(self):
				print "hii"
		
		
		def sub1(self):
			print "hii"
		
		
		
		def sub2(self):
			
			print "hii"
		
			
		def add(self,x,y):
			self.x=self.x+self.a1
			self.y=self.y+self.c
			print self.x
			print self.y
			self.x=x+self.a1
			self.y=y+self.c
			print self.x
			print self.y
		@classmethod
		def add1(cls):
			print "harshul"
		@staticmethod
		def s():
			print "uttu"

			
	a2=d(10,15)
	d.add(a2,15,20)
	d.add1()
	d.s()

	
	print a.a1"""
	class Mammal(object):
		def __init__(self, mammalName):
			print(mammalName, 'is a warm-blooded animal.')
		__var__=5
    
	class Dog(Mammal):
		def __init__(self):
			print('Dog has four legs.')
			super(Dog,self).__init__('Dog')
			print Mammal.__var__
    
	d1 = Dog()
	
	