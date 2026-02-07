"""Test script to verify the PAChT hydraulics modules work correctly."""

import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PAChT_quizes.constants import MOLECULAR_MASSES
from PAChT_quizes.hydraulics import gas_density, pressure_static
from PAChT_quizes.gas_properties import gas_volume
from PAChT_quizes.fluid_mechanics import equi_diameter_hull_tube


def test_modules():
    """Test that all modules can be imported and basic functions work."""
    print("Testing PAChT hydraulics modules...")
    
    # Test constants
    assert "CO2" in MOLECULAR_MASSES
    assert MOLECULAR_MASSES["CO2"] == 44
    print("✓ Constants module loaded correctly")
    
    # Test hydraulics functions
    density = gas_density(MOLECULAR_MASSES["CO2"], 90, 1.2)
    assert density > 0
    print(f"✓ gas_density function works: {density:.2f} kg/m³")
    
    pressure = pressure_static(1000, 10)
    assert pressure > 0
    print(f"✓ pressure_static function works: {pressure:.2f} Pa")
    
    # Test gas properties functions
    volume = gas_volume(100, 200000, 50)
    assert volume > 0
    print(f"✓ gas_volume function works: {volume:.2f} m³")
    
    # Test fluid mechanics functions
    eq_diameter = equi_diameter_hull_tube(61, 0.038, 0.625)
    assert eq_diameter > 0
    print(f"✓ equi_diameter_hull_tube function works: {eq_diameter:.4f} m")
    
    print("\nAll tests passed! The modules are working correctly.")


if __name__ == "__main__":
    test_modules()