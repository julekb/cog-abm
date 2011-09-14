import sys
sys.path.append('../')
import unittest
import random
from cog_abm.stimuli.stimulus import *
from cog_abm.extras.color import Color

class TestColor(unittest.TestCase):
	
	def test_init_stimulus(self):
		"""
		Test of giving random content to the color instance.
		"""
		
		stimul = Stimulus()
		self.assertEqual(isinstance(stimul, Stimulus), True)
		
	def test_init_stimulusColor(self):
		"""
		Test of giving random content to the color instance.
		"""
		random.seed()
		L = random.random()
		a = random.randint(0, 255)
		b = random.randint(0, 255)        
		col = Color(L, a, b)
		stimul_col = SimpleStimulus(col)
		self.assertEqual(stimul_col.content, col)
		self.assertEqual(stimul_col.content.to_ML_data(), [L, a, b])
		self.assertEqual(isinstance(stimul_col, Stimulus), True)
		self.assertEqual(isinstance(stimul_col, SimpleStimulus), True)
	
	
if __name__ == '__main__':
	unittest.main()
	
