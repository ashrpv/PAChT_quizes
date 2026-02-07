"""Gas properties module for applied hydraulics calculations."""


def gas_volume(normal_volume, pressure, temperature, normal_pressure=1, normal_temperature=0):
    """
    Recalculate gas volume from normal conditions to required conditions.
    
    Args:
        normal_volume: Volume at normal conditions
        pressure: Pressure in Pa
        temperature: Temperature in Celsius
        normal_pressure: Normal pressure (default 1 atm)
        normal_temperature: Normal temperature in Celsius (default 0°C)
        
    Returns:
        Volume at specified conditions
    """
    return normal_volume * (273.15 + temperature) * normal_pressure / (pressure * (273.15 + normal_temperature))


def gas_mixture_viscosity(viscosities, volumes, masses):
    """
    Calculate viscosity of a gas mixture.
    
    Args:
        viscosities: List of viscosities of components
        volumes: List of volume fractions
        masses: List of molecular masses
        
    Returns:
        Viscosity of the mixture
    """
    n = len(viscosities)
    mixture_mass = 0
    adjusted_viscs = 0
    
    for i in range(n):
        partial_mass = volumes[i] * masses[i]
        mixture_mass += partial_mass
        adjusted_viscs += partial_mass / viscosities[i]
        
    return mixture_mass / adjusted_viscs


def gas_viscosity_temp(mu, temperature, constant=100):
    """
    Calculate gas viscosity at different temperatures.
    
    Args:
        mu: Reference viscosity
        temperature: Temperature in Kelvin
        constant: Constant (default 100)
        
    Returns:
        Viscosity at temperature
    """
    return mu * (((273.15 + constant) / (temperature + constant)) * (temperature / 273.15)**1.5)