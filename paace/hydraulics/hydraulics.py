"""Hydraulics module for applied hydraulics calculations."""

from .constants import GRAVITY


def gas_density(molecular_mass, t, p):
    """
    Calculate gas density at given temperature and pressure.
    
    Args:
        molecular_mass: Molecular mass
        t: Temperature in Celsius
        p: Pressure in atm
        
    Returns:
        Gas density in kg/m3
    """
    # Temperature should be entered in degrees Celsius, pressure - in atm
    # Result in kg/m3
    return (molecular_mass * 273 * p) / (273 + t)


def pressure_static(rho, h):
    """
    Calculate static pressure using the basic hydrostatic equation.
    
    Args:
        rho: Density in kg/m3
        h: Height in meters
        
    Returns:
        Pressure in Pa
    """
    # Density and height should be provided in SI units
    return rho * h * GRAVITY


def hydrostatic_pressure_kgs(rho, h):
    """
    Calculate hydrostatic pressure in kgf/cm2.
    
    Args:
        rho: Density in kg/m3
        h: Height in meters
        
    Returns:
        Pressure in kgf/cm2
    """
    return rho * h / 10**4


def hydraulic_press(d_small, d_large, force):
    """
    Calculate force multiplication in a hydraulic press.
    
    Args:
        d_small: Diameter of small piston in mm
        d_large: Diameter of large piston in mm
        force: Input force
        
    Returns:
        Output force
    """
    ratio = (d_large / d_small) ** 2
    return force * ratio