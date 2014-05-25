from yggdrasil.core import System, Component


class ExampleComponent(Component):
	_last_id = 0

	def __init__(self):
		self.name = ExampleComponent._last_id
		ExampleComponent._last_id += 1


class ExampleSystem(System):
	def __init__(self):
		self.componenttypes = (ExampleComponent,)

		#: The names of the entities processed in the last call to process
		self.names = []

	def process(self, world, components):
		self.names = []
		for c in components:
			self.names.append(c.name)
