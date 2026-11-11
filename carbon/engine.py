"""Industrial SCADA Energy Telemetry, Scope 1, 2, 3 GHG Carbon Accounting Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class EnergyMeterTelemetry:
    meter_id: str
    active_power_kw: float
    reactive_power_kvar: float
    power_factor: float
    daily_consumption_kwh: float


@dataclass
class CarbonFootprintReport:
    scope_1_direct_diesel_co2e_kg: float
    scope_2_indirect_grid_co2e_kg: float
    scope_3_freight_logistics_co2e_kg: float
    total_carbon_emissions_co2e_tonnes: float
    is_within_quarterly_cap: bool
    carbon_credits_required: float


class ScadaCarbonAccountingEngine:
    """Industrial GHG Protocol emissions and SCADA power telemetry tracker."""

    DIESEL_EMISSION_FACTOR = 2.68
    GRID_ELECTRICITY_EMISSION_FACTOR = 0.716
    FREIGHT_EMISSION_FACTOR = 0.105

    def calculate_footprint(
        self,
        diesel_litres_consumed: float,
        grid_kwh_consumed: float,
        freight_tonne_km: float,
        quarterly_cap_tonnes: float = 100.0
    ) -> CarbonFootprintReport:
        scope_1_kg = round(diesel_litres_consumed * self.DIESEL_EMISSION_FACTOR, 2)
        scope_2_kg = round(grid_kwh_consumed * self.GRID_ELECTRICITY_EMISSION_FACTOR, 2)
        scope_3_kg = round(freight_tonne_km * self.FREIGHT_EMISSION_FACTOR, 2)

        total_kg = scope_1_kg + scope_2_kg + scope_3_kg
        total_tonnes = round(total_kg / 1000.0, 3)

        within_cap = total_tonnes <= quarterly_cap_tonnes
        credits_needed = max(0.0, round(total_tonnes - quarterly_cap_tonnes, 2))

        return CarbonFootprintReport(
            scope_1_direct_diesel_co2e_kg=scope_1_kg,
            scope_2_indirect_grid_co2e_kg=scope_2_kg,
            scope_3_freight_logistics_co2e_kg=scope_3_kg,
            total_carbon_emissions_co2e_tonnes=total_tonnes,
            is_within_quarterly_cap=within_cap,
            carbon_credits_required=credits_needed
        )
