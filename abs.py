from abc import abstractmethod

 
class AbstractOperation():
 
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        
    
    @abstractmethod
    def execute(self):
        pass


class b(AbstractOperation):
	def __init__(self):
		self.operand_a=20
		self.operand_b=10
		
		
a=b()	