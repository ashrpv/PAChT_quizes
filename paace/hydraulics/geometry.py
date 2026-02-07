"""Geometry module for applied hydraulics calculations."""


def hydr_r_ring(r_inner, r_outer):
    """
    Calculate hydraulic radius for ring cross-section.
    
    Args:
        r_inner: Inner radius
        r_outer: Outer radius
        
    Returns:
        Hydraulic radius
    """
    return 2 / 3 * (r_outer - r_inner)


def hydr_r_square(a):
    """
    Calculate hydraulic radius for square cross-section.
    
    Args:
        a: Side length
        
    Returns:
        Hydraulic radius
    """
    return 0.25 * a


def hydr_r_rectangle(a, b):
    """
    Calculate hydraulic radius for rectangular cross-section.
    
    Args:
        a: Side length 1
        b: Side length 2
        
    Returns:
        Hydraulic radius
    """
    return 0.5 / (1 / a + 1 / b)


def hydr_r_triangle(a):
    """
    Calculate hydraulic radius for equilateral triangle cross-section.
    
    Args:
        a: Side length
        
    Returns:
        Hydraulic radius
    """
    return a / (4 * 3 ** 0.5)