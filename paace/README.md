# PAChT Hydraulics Package

This directory contains the modularized version of the PAChT hydraulics calculations.

## Structure

- `hydraulics/` - The main Python package with modularized hydraulics functions
  - `constants.py` - Physical constants and molecular masses
  - `hydraulics.py` - Core hydraulic calculations
  - `gas_properties.py` - Gas property calculations
  - `fluid_mechanics.py` - Fluid mechanics calculations
  - `geometry.py` - Geometric calculations
  - `demo.py` - Example usage of the modules
  - `test_modules.py` - Test script to verify the modules work correctly
- `1_applied_hydraulics_modular.ipynb` - Jupyter notebook demonstrating the use of the modularized code
- `test_hydraulics.py` - Test script to verify the package works correctly

## Usage

To use the hydraulics package, you can import the modules as follows:

```python
from hydraulics.constants import MOLECULAR_MASSES
from hydraulics.hydraulics import gas_density, pressure_static
from hydraulics.gas_properties import gas_volume
from hydraulics.fluid_mechanics import equi_diameter_hull_tube
```

## Testing

To test the package, run:

```bash
python test_hydraulics.py
```

Or from within the paace directory:

```bash
cd paace
python test_hydraulics.py