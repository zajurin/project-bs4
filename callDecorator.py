from decorators import decorator_function	


@decorator_function
def suma():
	resultado = 20+15
	print(resultado)
	
@decorator_function
def subtract():
	resultado = 18-3
	print(resultado)
	


suma()
subtract()