import unittest
from PowerSource import PowerSource
from PowerSource import FixedPowerSource
from PowerSource import VariablePowerSource
from PowerSource import PowerStorageSource

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
        powerThresholds = [[1, 6], [2, 10], [3, 6], [7, 10]]
        testSource.set_power_thresholds(powerThresholds)

        # Check to make sure the power outputs fall within the thresholds
        for timeIndex in range(0, 4):
            powerOutput = testSource.get_power_output(timeIndex)
            self.assertGreaterEqual(powerOutput, powerThresholds[timeIndex][0])
            self.assertLessEqual(powerOutput, powerThresholds[timeIndex][1])


    def test_power_storage(self):
        testSource = PowerStorageSource()
        testCapacity = 100
        testCharge = 80

        # Set capacity and charge.
        testSource.set_capacity(testCapacity)
        testSource.add_charge(testCharge)

        # Check the capacity and charge.
        self.assertEqual(testSource.get_capacity(), testCapacity)
        self.assertEqual(testSource.get_charge(), testCharge)

        # Use power and check charge.
        testSource.use_power(50)
        self.assertEqual(testSource.get_charge(), 30)


    def test_overcharge_undercharge(self):
        testSource = PowerStorageSource()
        testCapacity = 100
        testCharge = 120

        # Set capacity and overcharge
        testSource.set_capacity(testCapacity)
        testSource.add_charge(testCharge)

        # Test overcharge.
        self.assertEqual(testSource.get_charge(), 100)

        # Draw too much power and test.
        testSource.use_power(150)
        self.assertEqual(testSource.get_charge(), 0)


if __name__ == "__main__":
    unittest.main()
