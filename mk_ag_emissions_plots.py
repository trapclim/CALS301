import matplotlib.pyplot as plt
import json

# Load the color palette
with open('colors.json', 'r') as f:
    colors_dict = json.load(f)

# Create a palette for the charts using Cornell colors
chart_colors = [
    colors_dict['cornell_colors']['carnelian']['base'],      
    colors_dict['cornell_colors']['carnelian']['light1'],    
    colors_dict['cornell_colors']['carnelian']['light2'],    
    colors_dict['cornell_colors']['secondary_red']['base'],  
    colors_dict['cornell_colors']['secondary_red']['light1'], 
    colors_dict['cornell_colors']['accent_gray']['base'],    
    colors_dict['cornell_colors']['accent_gray']['light1']   
]

# Figure 1: Pie chart of agricultural emission sources
emission_sources = {
    'Enteric fermentation': 23,  
    'Forest conversion': 27,     
    'Manure management': 2.5,    
    'Manure on pasture': 8.5,    
    'Synthetic fertilizers': 5,  
    'Crop residues': 1.4,        
    'Other (e.g., rice cultivation,\nsoil management, burning)': 32.6  # Added definition
}

# Calculate total GtCO2e for 2021
total_emissions = 10.89  # 2021 value
plt.figure(figsize=(10, 8))
plt.pie(emission_sources.values(), 
        labels=[f'{k}\n({v}%)' for k, v in emission_sources.items()],
        colors=chart_colors,
        autopct=None,  # Removed percentages inside the wedges
        pctdistance=0.85,
        wedgeprops={'edgecolor': colors_dict['cornell_colors']['white']['base'], 
                   'linewidth': 1})

plt.title(f'Agricultural GHG Emission Sources (2021)\nTotal: {total_emissions:.2f} GtCO2e', 
         pad=20, 
         color=colors_dict['cornell_colors']['carnelian']['base'],
         weight='bold',
         size=14)

plt.savefig('agricultural_sources.png', 
            bbox_inches='tight', 
            dpi=300, 
            facecolor=colors_dict['cornell_colors']['white']['base'])
plt.close()

# Figure 2: Bar chart of 2050 projections
scenarios = [
    'Current trends',
    'Double forest\nconservation',
    'Triple forest\nconservation'
]
emissions = [11.82, 10.89, 9.85]
error = [0.07, 0, 0.07]

plt.figure(figsize=(10, 6))
bars = plt.bar(scenarios, emissions, 
               yerr=error,
               capsize=5,
               color=[colors_dict['cornell_colors']['carnelian']['base'],
                     colors_dict['cornell_colors']['secondary_red']['base'],
                     colors_dict['cornell_colors']['accent_gray']['base']])

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', 
             va='bottom',
             color=colors_dict['cornell_colors']['gray']['base'])

plt.ylabel('GHG Emissions (GtCO2e)',
          color=colors_dict['cornell_colors']['gray']['base'])

plt.title('Agricultural Emissions Projections for 2050\nProjected range: 9.85-11.82 GtCO2e', 
         pad=20,
         color=colors_dict['cornell_colors']['carnelian']['base'],
         weight='bold',
         size=14)

# Add gridlines with Cornell gray color
plt.grid(axis='y', 
         linestyle='--', 
         alpha=0.7,
         color=colors_dict['cornell_colors']['accent_gray']['light2'])

# Set background color
plt.gca().set_facecolor(colors_dict['cornell_colors']['white']['base'])
plt.gcf().set_facecolor(colors_dict['cornell_colors']['white']['base'])

plt.savefig('agricultural_projections.png', 
            bbox_inches='tight', 
            dpi=300,
            facecolor=colors_dict['cornell_colors']['white']['base'])
plt.close()