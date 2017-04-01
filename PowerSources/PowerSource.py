
class PowerSource(object):
    """The base class for power sources, which acts as an interface for all the power sources."""
    def __init__(self):
        self.capacity = -1
        self.power_output = 0

    def get_capacity(self):
        return self.capacity

    def get_power_output(self, timeOfDay):
        return self.power_output


class FixedPowerSource(PowerSource):
    """The power source object that sets a fixed power output."""
    def __init__(self):
        super(FixedPowerSource, self).__init__()

    def set_power_output(self, output):
        self.power_output = output


class VariablePowerSource(PowerSource):
    """docstring for VariablePowerSource."""
    def __init__(self):
        super(VariablePowerSource, self).__init__()
        self.powerThresholds = []

    def set_power_thresholds(self, thresholds):
        self.powerThresholds = thresholds

    def get_power_output(self, timeOfDay):
        if timeOfDay < 4 and timeOfDay >= 0:
            return (self.powerThresholds[timeOfDay][0] + self.powerThresholds[timeOfDay][1]) / 2
