# Greenhouse Utility Planner
Model to plan utilities in a horticulture greenhouse, like electricity, heat and carbon dioxide

## Installation

## Model description

### Goal of the model
The goal of the model is to determine the optimal combination of utilities for a greenhouse for minimized emissions and maximized crops production.

### Model scope
The model has the following scope:
- The model determines the operation schedule for a greenhouse over a period of a year, with an hourly timestep.
- The model can handle one type of crop, and one type of greenhouse. The model can handle multiple utilities, and multiple sources for each utility.
- The default crop type is tomato, and the default greenhouse type is a greenhouse with a glass roof.
- The demand for heat, cooling, lighting, ventilation and irrigation is determined by the crop type and the greenhouse type.

### Model input variables
The model requires the following input variables:
1. `location`: Location of the greenhouse (default is `Rotterdam`)
2. `area`: Area of the greenhouse in m²
3. `crop`: Crop to be grown in the greenhouse
4. `utilities`: selection utilities (zero capacity = not installed)
   - `installed capacity of combined heat and power installation (CHP)`: power of the CHP installation in MW
   - `installed capacity of heat pump`: heat pump capacity installed in MW
   - `installed capacity geo thermal`: geo thermal installation capacity in MW
   - `installed capacity of solar thermal`: power of the solar thermal installation in MW
   - `installed capacity solar panels`: installed capacity solar panels in MW
   - `installed capacity wind turbines`: installed capacity wind turbines in MW
   - `power connection the grid`: size of power connection to the grid in MW
   - `direct air capture capacity`: direct air capture capacity in tonnes of CO2 per hour
   - `liquid by truck`: liquid CO2 by truck installed or not (true or false)
5. `cooling sources`: selection of cooling sources
6. `lighting sources`: selection of lighting sources
7. `ventilation sources`: selection of ventilation sources
8. `irrigation sources`: selection of irrigation sources

### Model constants and parameters
The model has the following constants:
 - `solar irradiation`: hourly distribution of solar irradiation in W/m²
 - `temperature`: hourly distribution of outside temperature in °C
 - `humidity`: hourly distribution of outside humidity in %
 - `wind speed`: hourly distribution of outside wind speed in m/s
 - `price natural gas`: price of natural gas in euros per m³
 - `price electricity`: price of electricity in euros per kWh
 - `price liquid CO2`: price of CO2 liquid in euros per tonne
 - `efficiency CHP`: efficiency of the CHP installation in %
 - `efficiency heat pump`: efficiency of the heat pump in %
 - `temperature geo thermal`: temperature of the geo thermal installation in °C
 - `efficiency solar thermal`: efficiency of the solar thermal installation in %
 - `efficiency solar panels`: efficiency of the solar panels in %
 - `efficiency wind turbines`: efficiency of the wind turbines in %
 - `enery consumption direct air capture`: energy consumption of the direct air capture in kWh per tonne of CO2
 - `buffer capacity direct air capture`: buffer capacity of the direct air capture in tonnes of CO2

### Model output variables
The model outputs the following variables:
1. `emissions`: emissions of the greenhouse in tonnes of CO2 over the modelling time period, with an hourly timestep
2. `total emissions`: emissions of the greenhouse in tonnes of CO2 over the modelling time period
3. `crop production`: crop production in tonnes over the modelling time period
4. `revenue`: revenue in euros over the modelling time period
5. `operation schedule`: operation schedule of the greenhouse over the modelling time period, with an hourly timestep
6. `emissions per utility`: emissions of the greenhouse per utility over the modelling time period, with an hourly timestep
7. `utilization rate per utility`: utilization rate of the greenhouse per utility in percentage

### Model structure
The model is structured as follows:
 - The greenhouse itself is an object, as well as every utility source. Every object has its own class. 
 - The greenhouse object has a method to calculate the greenhouse demand for heat, cooling, lighting, ventilation and irrigation based on the crop type, weather conditions, the greenhouse type, and operation strategy.
 - The greenhouse object has a method to calculate crop yield, crop production, and revenue over the time period.
 - The system as total can call the greenhouse and utility objects, and makes sure the energy and mass balances are met.
 - The utility objects have a method to calculate the emissions of the utility source, the utilization rate, the consumption of their respective consumables (e.g. natural gas).

### Model assumptions




## Usage


## Contributing


## Chat GPT
Can you write a set of Python scripts for the model described below? Please also propose a project structure for the scripts. 