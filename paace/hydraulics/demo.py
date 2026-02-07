"""Demo script showing how to use the PAChT hydraulics modules."""

from .constants import MOLECULAR_MASSES
from .hydraulics import gas_density, pressure_static
from .gas_properties import gas_volume
from .fluid_mechanics import equi_diameter_hull_tube


def main():
    """Run demonstration examples."""
    # Example 1: Calculate gas density
    print("Example 1: Calculate gas density")
    density = gas_density(MOLECULAR_MASSES["CO2"], 90, 1.2)
    print(f"Density of CO2 at 90°C and 1.2 atm: {density:.2f} kg/m³")
    
    # Example 2: Calculate static pressure
    print("\nExample 2: Calculate static pressure")
    pressure = pressure_static(1000, 10)
    print(f"Pressure at 10m depth in liquid with density 1000 kg/m³: {pressure:.2f} Pa")
    
    # Example 3: Calculate gas volume at different conditions
    print("\nExample 3: Calculate gas volume at different conditions")
    volume = gas_volume(100, 200000, 50)
    print(f"Volume of gas at 2 bar and 50°C: {volume:.2f} m³")
    
    # Example 4: Calculate equivalent diameter for heat exchanger
    print("\nExample 4: Calculate equivalent diameter for heat exchanger")
    eq_diameter = equi_diameter_hull_tube(61, 0.038, 0.625)
    print(f"Equivalent diameter for heat exchanger with 61 tubes: {eq_diameter:.4f} m")


if __name__ == "__main__":
    main()