# PAChT Hydraulics Package

This package contains modules for applied hydraulics calculations, extracted from the `1_applied_hydraulics.ipynb` Jupyter notebook.

## Modules

### constants.py
Contains physical constants and molecular masses:
- GRAVITY: Gravitational acceleration (9.81 m/s²)
- STANDARD_PRESSURE_PA: Standard atmospheric pressure (101325 Pa)
- STANDARD_TEMPERATURE_K: Standard temperature (273.15 K)
- MMHG_TO_PA: Conversion factor from mmHg to Pa (133.322)
- MOLECULAR_MASSES: Dictionary of molecular masses for common gases

### hydraulics.py
Core hydraulic calculations:
- `gas_density()`: Calculate gas density at given temperature and pressure
- `pressure_static()`: Calculate static pressure using hydrostatic equation
- `hydrostatic_pressure_kgs()`: Calculate hydrostatic pressure in kgf/cm²
- `hydraulic_press()`: Calculate force multiplication in hydraulic press

### gas_properties.py
Gas property calculations:
- `gas_volume()`: Recalculate gas volume from normal to specified conditions
- `gas_mixture_viscosity()`: Calculate viscosity of gas mixtures
- `gas_viscosity_temp()`: Calculate gas viscosity at different temperatures

### fluid_mechanics.py
Fluid mechanics calculations:
- `reynolds_tube_tube()`: Calculate Reynolds number for tube-in-tube flow
- `regime_tube_tube()`: Determine flow regime for tube-in-tube heat exchangers
- `velocity_tube_tube()`: Calculate velocity in tube-in-tube heat exchangers
- `velocity_hull_tube()`: Calculate velocity in shell-and-tube heat exchangers
- `equi_diameter_tube_tube()`: Calculate equivalent diameter for tube-in-tube
- `equi_diameter_hull_tube()`: Calculate equivalent diameter for shell-and-tube

### geometry.py
Geometric calculations:
- `hydr_r_ring()`: Hydraulic radius for ring cross-section
- `hydr_r_square()`: Hydraulic radius for square cross-section
- `hydr_r_rectangle()`: Hydraulic radius for rectangular cross-section
- `hydr_r_triangle()`: Hydraulic radius for triangular cross-section

## Usage

Import the modules and use the functions as needed:

```python
from PAChT_quizes.constants import MOLECULAR_MASSES
from PAChT_quizes.hydraulics import gas_density

# Calculate density of CO2 at 90°C and 1.2 atm
density = gas_density(MOLECULAR_MASSES["CO2"], 90, 1.2)
```

## Examples

See `demo.py` for usage examples of the various functions.