"""Fluid mechanics module for applied hydraulics calculations."""

import math


def reynolds_tube_tube(flow_rate, tube_inner, tube_outer, mu, rho):
    """
    Calculate Reynolds number for flow in tube-in-tube heat exchanger.
    
    Args:
        flow_rate: Flow rate in m^3/h
        tube_inner: Inner tube diameter in m
        tube_outer: Outer tube diameter in m
        mu: Dynamic viscosity in Pa*s
        rho: Density in kg/m3
        
    Returns:
        Reynolds number
    """
    velocity = velocity_tube_tube(flow_rate, tube_inner, tube_outer)
    equi_dia = equi_diameter_tube_tube(tube_inner, tube_outer)
    return velocity * equi_dia * rho / mu


def regime_tube_tube(flow_rate, tube_inner, tube_outer, mu, rho):
    """
    Determine flow regime for tube-in-tube heat exchanger.
    
    Args:
        flow_rate: Flow rate in m^3/h
        tube_inner: Inner tube diameter in m
        tube_outer: Outer tube diameter in m
        mu: Dynamic viscosity in Pa*s
        rho: Density in kg/m3
        
    Returns:
        Flow regime as string
    """
    re = reynolds_tube_tube(flow_rate, tube_inner, tube_outer, mu, rho)
    
    if re <= 2300:
        return 'Ламинарное течение'
    elif re <= 10000:
        return 'Переходное течение'
    else:
        return 'Турбулентное течение'


def velocity_tube_tube(flow_rate, tube_inner, tube_outer):
    """
    Calculate velocity in tube-in-tube heat exchanger.
    
    Args:
        flow_rate: Flow rate in m^3/h
        tube_inner: Inner tube diameter in m
        tube_outer: Outer tube diameter in m
        
    Returns:
        Velocity in m/s
    """
    return velocity_hull_tube(flow_rate, 1, tube_inner, tube_outer)


def velocity_hull_tube(flow_rate, n_tubes, tube_outer_d, hull_inner_d):
    """
    Calculate velocity in shell-and-tube heat exchanger.
    
    Args:
        flow_rate: Flow rate in m^3/h
        n_tubes: Number of tubes
        tube_outer_d: Outer tube diameter in m
        hull_inner_d: Inner shell diameter in m
        
    Returns:
        Velocity in m/s
    """
    # Flow in m^3/h, velocity in m/s
    area = math.pi / 4 * (hull_inner_d ** 2 - n_tubes * tube_outer_d ** 2)
    return flow_rate / (3600 * area)


def equi_diameter_tube_tube(tube_inner_d, tube_outer_d):
    """
    Calculate equivalent diameter for tube-in-tube heat exchanger.
    
    Args:
        tube_inner_d: Inner tube diameter in m
        tube_outer_d: Outer tube diameter in m
        
    Returns:
        Equivalent diameter in m
    """
    return equi_diameter_hull_tube(1, tube_inner_d, tube_outer_d)


def equi_diameter_hull_tube(n_tubes, tube_outer_d, hull_inner_d):
    """
    Calculate equivalent diameter for shell-and-tube heat exchanger.
    
    Args:
        n_tubes: Number of tubes
        tube_outer_d: Outer tube diameter in m
        hull_inner_d: Inner shell diameter in m
        
    Returns:
        Equivalent diameter in m
    """
    area = math.pi / 4 * (hull_inner_d ** 2 - n_tubes * tube_outer_d ** 2)
    perimeter = math.pi * (hull_inner_d + n_tubes * tube_outer_d)
    return 4 * area / perimeter