# Data source: https://pmc.ncbi.nlm.nih.gov/articles/PMC11683860/
# Visualizing 2024 atmospheric GHG concentrations and their relative global warming potentials

import matplotlib.pyplot as plt
import numpy as np
import json

# Load the Cornell color scheme
with open('colors.json', 'r') as f:
    colors = json.load(f)

# Extract some colors for our visualization
bar_colors = [
    colors['cornell_colors']['carnelian']['base'],
    colors['cornell_colors']['secondary_red']['base'],
    colors['cornell_colors']['accent_gray']['base']
]

# Data explicitly stated in the article for 2024
ghg_data = {
    'Gas': ['CO2', 'CH4', 'N2O'],
    'Concentration': [423, 1932, 338],  # ppm for CO2, ppb for CH4 and N2O
    'GWP': [1, 28, 265]  # Global Warming Potential over 100-year time scale
}

# Create figure and axes with white background
plt.rcParams['axes.facecolor'] = colors['cornell_colors']['white']['base']
plt.rcParams['figure.facecolor'] = colors['cornell_colors']['white']['base']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot 1: Atmospheric Concentrations
bars1 = ax1.bar(['CO2 (ppm)', 'CH4 (ppb)', 'N2O (ppb)'], 
                ghg_data['Concentration'],
                color=bar_colors)

ax1.set_title('Atmospheric Concentrations (2024)', 
              color=colors['cornell_colors']['gray']['base'],
              pad=20)
ax1.set_ylabel('Concentration', 
               color=colors['cornell_colors']['gray']['base'])
ax1.tick_params(colors=colors['cornell_colors']['gray']['base'])

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom',
             color=colors['cornell_colors']['gray']['base'])

# Plot 2: Global Warming Potentials
bars2 = ax2.bar(ghg_data['Gas'], 
                ghg_data['GWP'],
                color=bar_colors)

ax2.set_title('Global Warming Potential\n(100-year time scale)', 
              color=colors['cornell_colors']['gray']['base'],
              pad=20)
ax2.set_ylabel('GWP (CO2 equivalent)', 
               color=colors['cornell_colors']['gray']['base'])
ax2.tick_params(colors=colors['cornell_colors']['gray']['base'])

# Add value labels on bars
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom',
             color=colors['cornell_colors']['gray']['base'])

# Style the grid and axes
for ax in [ax1, ax2]:
    ax.grid(True, linestyle='--', alpha=0.7, 
            color=colors['cornell_colors']['gray']['light4'])
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_color(colors['cornell_colors']['gray']['light3'])

# Adjust layout and add citation
plt.tight_layout()
fig.text(0.1, 0.02, 'Source: Global Change Biology (2024)', 
         fontsize=8, style='italic',
         color=colors['cornell_colors']['gray']['base'])

# Save the plot
plt.savefig('ghg_concentrations_gwp_2024.png', 
            bbox_inches='tight', 
            dpi=300,
            facecolor=fig.get_facecolor(),
            edgecolor='none')
plt.savefig('ghg_concentrations_gwp_2024.pdf',
            bbox_inches='tight', 
            dpi=300,
            facecolor=fig.get_facecolor(),
            edgecolor='none')