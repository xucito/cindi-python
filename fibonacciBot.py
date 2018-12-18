from cindi_python import CindiHandler

class FibonacciBot(CindiHandler):
	pass
	def HandleStep(step):
		if step.template.name == '':
			firstNumber = step.inputs['n-1']
			secondNumber = step.inputs['n-2']
			step.outputs = {
				"n": firstNumber+secondNumber
			}
		return step