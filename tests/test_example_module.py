import unittest
from yggdrasil.core import World, Entity
from yggdrasil.modules.example import ExampleComponent, ExampleSystem


class TestExampleSystem(unittest.TestCase):
	class ExampleEntity(Entity):
		def __init__(self, world):
			self.examplecomponent = ExampleComponent()

	def test_process(self):
		world = World()
		es = ExampleSystem()
		world.add_system(es)

		[self.ExampleEntity(world) for i in range(10)]

		world.process()
		for i in range(10):
			self.assertTrue(i in es.names, str(i) + " not in es.names")

if __name__ == '__main__':
	unittest.main()