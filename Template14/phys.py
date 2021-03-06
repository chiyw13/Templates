# this is a class of physics
# this could be used to get physical constants 
# also used for unit conversion
# m represent '-'
# p represent '+'
import numpy as np

class phys:
	# all SI unit used for the physical constants
	# plank constant
	h = 6.62606957E-34
	# light speed
	c = 299792458
	# gas constant
	R = 8.314
	# 1 atm to Pa
	atm = 101325
	# avogadro constant
	NA = 6.022e23

	def __init__(self,h=6.62606957E-34,c=299792458):
		self.h = h
		self.c = c

	def hatreeToJoul(self, E):
		return E*4.35974434E-18

	# hatree to cm^-1
	def hatreeTocmm1(self, E):
		return self.hatreeToJoul(E)/self.h/self.c/100

	def degreeTorad(self, alpha):
		return alpha/180*np.pi

	def calToJoul(self, E):
		return E*4.184


