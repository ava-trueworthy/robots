import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegValues.npy")
frontLegSensorValues = numpy.load("data/frontLegValues.npy")

matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg Sensor Values", linewidth=2.5)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg Sensor Values")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
