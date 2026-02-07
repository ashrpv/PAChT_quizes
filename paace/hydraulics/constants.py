"""Constants module for applied hydraulics calculations."""

# Physical constants
GRAVITY = 9.81  # m/s^2
STANDARD_PRESSURE_PA = 101325  # Pa (1 atm)
STANDARD_TEMPERATURE_K = 273.15  # K (0°C)
MMHG_TO_PA = 133.322  # Conversion factor from mmHg to Pa

# Molecular masses
MOLECULAR_MASSES = {
    "CO2": 44,
    "N2": 28,
    "H2O": 18,
    "H2": 2,
    "CO": 28
}