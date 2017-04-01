import unittest
from PowerSource import PowerSource
from PowerSource import FixedPowerSource
from PowerSource import VariablePowerSource

class PowerSourceTests(unittest.TestCase):
    """Unit tests for the power source objects."""
    def test_default_power_output(self):
        testSource = PowerSource()

        # Check for default power output and capacity.
        self.assertEqual(testSource.get_power_output(1), 0)
        self.assertEqual(testSource.get_capacity(), -1)


    def test_fixed_power_output(self):
        testSource = FixedPowerSource()

        # Set a power output and test to make sure it has been saved.
        testPowerOutput = 10
        testSource.set_power_output(testPowerOutput)
        self.assertEqual(testSource.get_power_output(0), testPowerOutput)
        self.assertEqual(testSource.get_capacity(), -1)


    def test_variable_power_output(self):
        testSource = VariablePowerSource()

        # Set power thresholds for each time.
        powerThresholds = [[1, 3], [2, 4], [3, 6], [4, 7]]
        testSource.set_power_thresholds(powerThresholds)

        # Check to make sure the power outputs fall within the thresholds
        for timeIndex in range(0, 4):
            powerOutput = testSource.get_power_output(timeIndex)
            self.assertGreater(powerOutput, powerThresholds[timeIndex][0])
            self.assertLess(powerOutput, powerThresholds[timeIndex][1])



if __name__ == "__main__":
    unittest.main()
