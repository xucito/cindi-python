from cindi_python import TemplateReference, StepTemplate, SetEncoder
import json
from fibonacciBot import FibonacciBot

fibonacciStep = StepTemplate("Fibonacci",
                             version=0,
                             inputDefinitions={
                                 "n-1": 0,
                                 "n-2": 0
                             },
                             outputDefinitions={
                                 "n": 0
                             })


#cindi_python.register("http://localhost:5021", [
#    fibonacciStep
#])

#cindi_python.start("http://localhost:5021")

fib = FibonacciBot(url="http://localhost:5021")
fib.registerTemplate(fibonacciStep)
fib.start()