import random

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
    """The power source object that sets random outputs within a set threshold."""
    def __init__(self):
        super(VariablePowerSource, self).__init__()
        self.powerThresholds = []

    def set_power_thresholds(self, thresholds):
        self.powerThresholds = thresholds

    def get_power_output(self, timeOfDay):
        random.seed()
        if timeOfDay < 4 and timeOfDay >= 0:
            return random.randint(self.powerThresholds[timeOfDay][0], self.powerThresholds[timeOfDay][1])

class PowerStorageSource(object):
    """The power storage object that acts as a battery or similar storage device."""
    def __init__(self):
        super(PowerStorageSource, self).__init__()
        self.charge = 0
        self.capacity = 0

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def add_charge(self, newCharge):
        self.charge += newCharge
        if self.charge > self.capacity:
            self.charge = self.capacity

    def get_charge(self):
        return self.charge

    def use_power(self, power):
        self.charge -= power
        if self.charge < 0:
            self.charge = 0
