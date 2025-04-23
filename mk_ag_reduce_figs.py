import matplotlib.pyplot as plt
import json
import numpy as np

# Load Cornell color palette
with open('colors.json', 'r') as f:
    colors_dict = json.load(f)

# Create color palette from Cornell colors
chart_colors = [
    colors_dict['cornell_colors']['carnelian']['base'],
    colors_dict['cornell_colors']['carnelian']['light1'],
    colors_dict['cornell_colors']['carnelian']['light2'],
    colors_dict['cornell_colors']['secondary_red']['base'],
    colors_dict['cornell_colors']['accent_gray']['base']
]

# Figure 1: Reduction potentials by strategy
reduction_data = {
    'On-farm energy use': 95,
    'Nitrogen management': 70,
    'Rice cultivation': 30,
    'Enteric fermentation': 55
}

plt.figure(figsize=(10, 6))
bars = plt.bar(reduction_data.keys(), reduction_data.values(), 
               color=chart_colors)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}%',
             ha='center', va='bottom',
             color=colors_dict['cornell_colors']['gray']['base'])

plt.ylabel('Reduction Potential (%)',
          color=colors_dict['cornell_colors']['gray']['base'])
plt.title('Maximum GHG Reduction Potential by Strategy',
         color=colors_dict['cornell_colors']['carnelian']['base'],
         pad=20,
         weight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('reduction_potentials.png', 
            bbox_inches='tight', 
            dpi=300,
            facecolor=colors_dict['cornell_colors']['white']['base'])
plt.close()

# Figure 2: Negative emissions potential and costs
fig, ax1 = plt.subplots(figsize=(10, 6))

technologies = ['BECCS', 'Enhanced Rock\nWeathering']
potentials = [2.61, 1.25]  # Using midpoint of 0.5-2.0 for ERW
costs_min = [100, 80]
costs_max = [200, 180]

# Bar plot for potentials
bars = ax1.bar(technologies, potentials, 
               color=[chart_colors[0], chart_colors[2]])
ax1.set_ylabel('Potential (GtCO2eq/year)',
               color=colors_dict['cornell_colors']['gray']['base'])

# Add cost ranges as text
for i, (cost_min, cost_max) in enumerate(zip(costs_min, costs_max)):
    plt.text(i, potentials[i], 
             f'${cost_min}-{cost_max}\nper ton CO2',
             ha='center', va='bottom')

plt.title('Carbon Removal Potential and Costs by Technology',
          color=colors_dict['cornell_colors']['carnelian']['base'],
          pad=20,
          weight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('negative_emissions_potential.png', 
            bbox_inches='tight', 
            dpi=300,
            facecolor=colors_dict['cornell_colors']['white']['base'])
plt.close()

# Figure 3: Pathway to net zero
current_emissions = 7.1
reduction = 7.1 * 0.45  # 45% reduction
residual = 7.1 * 0.55   # 55% remaining
total_removal_potential = 2.61 + 1.25  # BECCS + ERW

steps = ['Current\nEmissions', 'After 45%\nReduction', 'Residual\nEmissions', 'Potential\nRemovals', 'Net\nEmissions']
values = [current_emissions, -reduction, residual, -total_removal_potential, 
          residual-total_removal_potential]

plt.figure(figsize=(12, 6))
bars = plt.bar(steps, values, 
               color=[chart_colors[0] if v > 0 else chart_colors[2] for v in values])

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., 
             height if height > 0 else height - 0.2,
             f'{height:.1f}',
             ha='center', va='bottom' if height > 0 else 'top',
             color=colors_dict['cornell_colors']['gray']['base'])

plt.ylabel('GtCO2eq/year',
          color=colors_dict['cornell_colors']['gray']['base'])
plt.title('Pathway to Net Zero in Agriculture',
         color=colors_dict['cornell_colors']['carnelian']['base'],
         pad=20,
         weight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.axhline(y=0, color=colors_dict['cornell_colors']['gray']['base'], 
            linestyle='-', linewidth=0.5)

plt.savefig('pathway_to_net_zero.png', 
            bbox_inches='tight', 
            dpi=300,
            facecolor=colors_dict['cornell_colors']['white']['base'])
plt.close()