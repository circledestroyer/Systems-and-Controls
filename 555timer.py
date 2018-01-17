def values(a,b,c):
    capacitance = c * (10**-6)
    thigh = 0.693 * (a + b) * capacitance
    period = 0.693 * (a + (2 * b)) * capacitance
    frequency = 1/period
    duty = (thigh / period) * 100
    tlow = period - thigh
    print "The period is " + str(period) + " seconds"
    print "The frequency is " + str(frequency) + " Hertz"
    print "The High Voltage Time is " + str(thigh) + " seconds"
    print "The Low Voltage Time is " + str(tlow) + " seconds"
    print "The duty cycle is " + str(duty) + " percent"