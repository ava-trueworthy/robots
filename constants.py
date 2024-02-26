"""
Store all constants used in simulate.py
"""

import numpy

"""
Vectors to send motor commands
"""
amplitude = numpy.pi/2
frequency = 10
offset = 0
maxForce = 500


amplitudeFrontLeg = numpy.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi/4
maxForceFrontLeg = 500

targetAnglesFrontLeg = numpy.linspace(0, 2*numpy.pi, num=1000)

for x in range(1000):
   targetAnglesFrontLeg[x] = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg*targetAnglesFrontLeg[x] + phaseOffsetFrontLeg)
"""
numpy.save("data/targetAnglesBackLeg.npy", targetAnglesBackLeg)
numpy.save("data/targetAnglesFrontLeg.npy", targetAnglesFrontLeg)
"""
