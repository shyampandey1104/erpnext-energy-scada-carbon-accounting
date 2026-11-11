import unittest
from carbon.engine import ScadaCarbonAccountingEngine

class TestScadaCarbonAccounting(unittest.TestCase):
    def test_carbon_footprint_calculation(self):
        engine = ScadaCarbonAccountingEngine()
        report = engine.calculate_footprint(
            diesel_litres_consumed=5000.0,
            grid_kwh_consumed=100000.0,
            freight_tonne_km=20000.0,
            quarterly_cap_tonnes=80.0
        )

        self.assertEqual(report.scope_1_direct_diesel_co2e_kg, 13400.0)
        self.assertEqual(report.scope_2_indirect_grid_co2e_kg, 71600.0)
        self.assertEqual(report.scope_3_freight_logistics_co2e_kg, 2100.0)
        self.assertEqual(report.total_carbon_emissions_co2e_tonnes, 87.1)
        self.assertFalse(report.is_within_quarterly_cap)
        self.assertEqual(report.carbon_credits_required, 7.1)

if __name__ == "__main__":
    unittest.main()
