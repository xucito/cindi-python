import requests
import json
import time
class CindiHandler:
	def __init__(self, url, stepTemplates = []):
		self.stepTemplates = stepTemplates
		self.url = url
	def HandleStep(step):
		return step
		
	def start(self, sleep = 3):
		jsonList = []
		headers = {'content-type': 'application/json'}
		for definition in self.stepTemplates:
			jsonList.append(json.dumps(definition.__dict__))
		while(True):
			result = requests.post(self.url + "/api/Steps/next", data = json.dumps(jsonList), headers = headers)
			response = result.text
			if response != 'null':
				self.HandleStep(json.loads(response))
			time.sleep(sleep)

	def registerTemplate(self, stepTemplate):
		headers = {'content-type': 'application/json'}
		result = requests.post(self.url + "/api/steptemplates", data = json.dumps(stepTemplate.__dict__, cls=SetEncoder), headers = headers)
		if result.status_code != 200:
			print("Error adding template" + stepTemplate.name + ", statuscode:" + str(result.status_code)) #+ ", message:" + result.json())
		else:
			self.stepTemplates.append(stepTemplate)

	def registerTemplates(self, stepTemplates):
		headers = {'content-type': 'application/json'}
		for template in stepTemplates:
			result = requests.post(self.url + "/api/steptemplates", data = json.dumps(template.__dict__, cls=SetEncoder), headers = headers)
			if result.status_code != 200:
				print("Error adding template" + template.name + ", statuscode:" + str(result.status_code)) #+ ", message:" + result.json())
			else:
				self.stepTemplates.append(template)
class Step:
	def __init__(self, id, inputs, createdOn):
		self.id = id
		self.inputs = inputs
		self.createdOn = createdOn

class TemplateReference:
	def __init__(self, name, version):
		self.name = name
		self.version = version
		self.templateId = name + ":" + str(version)

class StepTemplate:
	def __init__(self, name, version, inputDefinitions, outputDefinitions):
		self.name = name
		self.version = version
		self.inputDefinitions = inputDefinitions
		self.outputDefinitions = outputDefinitions

class SetEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, set):
			return list(obj)
		return json.JSONEncoder.default(self, obj)