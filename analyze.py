import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegValues.npy")
frontLegSensorValues = numpy.load("data/frontLegValues.npy")
targetAnglesBackLeg = numpy.load("data/targetAnglesBackLeg.npy")
targetAnglesFrontLeg = numpy.load("data/targetAnglesFrontLeg.npy")

matplotlib.pyplot.plot(targetAnglesBackLeg, linewidth=2.5)
matplotlib.pyplot.plot(targetAnglesFrontLeg)

"""
matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor Values", linewidth=2.5)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor Values")
matplotlib.pyplot.legend()
"""
matplotlib.pyplot.show()
