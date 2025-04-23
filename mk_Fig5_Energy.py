import matplotlib.pyplot as plt
import numpy as np
import colorsys

# Function to create lighter/darker variants of a base color
def create_color_variants(base_color, num_variants):
    # Convert hex to RGB
    base_rgb = tuple(int(base_color.lstrip('#')[i:i+2], 16)/255 for i in (0, 2, 4))
    # Convert RGB to HSV
    base_hsv = colorsys.rgb_to_hsv(*base_rgb)
    
    variants = [base_color]
    # Create lighter versions by adjusting saturation and value
    for i in range(num_variants):
        new_sat = max(0.3, base_hsv[1] - (i+1)*0.2)
        new_val = min(0.95, base_hsv[2] + (i+1)*0.1)
        new_rgb = colorsys.hsv_to_rgb(base_hsv[0], new_sat, new_val)
        new_hex = '#{:02x}{:02x}{:02x}'.format(
            int(new_rgb[0]*255),
            int(new_rgb[1]*255),
            int(new_rgb[2]*255)
        )
        variants.append(new_hex)
    return variants

# Base colors (from Fig 1)
base_colors = {
    'energy': '#3A708B',     # Hyperlink blue
    'process': '#FBB040',    # Gold
    'agriculture': '#8DC440', # Money green
    'waste': '#393F47'       # eC Black
}

# Create color variants for each sector
energy_colors = create_color_variants(base_colors['energy'], 3)
process_colors = create_color_variants(base_colors['process'], 2)
agriculture_colors = create_color_variants(base_colors['agriculture'], 2)
waste_colors = create_color_variants(base_colors['waste'], 1)

# Detailed data structure with categories and subcategories
emissions_data = {
    'Energy': {
        'Power': 26,
        'Industry': 11,
        'Transport': {
            'Aviation': 2,
            'Road': 11,
            'Other': 2
        },
        'Buildings': 6,
        'Fuel Production': {
            'Oil and gas': 3,
            'Solid fuels': 4,
            'Other': 3
        }
    },
    'Process': {
        'Industrial Processes': {
            'Cement': 3,
            'Chemicals': 2,
            'Metals': 1,
            'Other': 4
        }
    },
    'Agriculture': {
        'Agriculture': {
            'Livestock': 6,
            'Biomass burning, soils and rice': 5
        },
        'LULUCF': 7
    },
    'Waste': {
        'Solid waste': 2,
        'Liquid waste': 2
    }
}

# Flatten the data structure and assign colors
flat_data = {}
colors_map = {}

def flatten_data(data, parent_category=None, color_list=None):
    for category, value in data.items():
        if isinstance(value, dict):
            # This is a subcategory
            flatten_data(value, category, color_list)
        else:
            # This is a leaf node
            label = f"{category}" if parent_category is None else f"{category}"
            flat_data[label] = value
            if color_list:
                colors_map[label] = color_list[len(colors_map) % len(color_list)]

# Flatten the data structure and assign colors
flatten_data(emissions_data['Energy'], 'Energy', energy_colors)
flatten_data(emissions_data['Process'], 'Process', process_colors)
flatten_data(emissions_data['Agriculture'], 'Agriculture', agriculture_colors)
flatten_data(emissions_data['Waste'], 'Waste', waste_colors)


# Organize data in ordered groups
emissions_groups = [
    # Energy - Power & Industry
    ('Power', 26),
    ('Industry', 11),
    
    # Energy - Transport group
    ('Transport - Aviation', 2),
    ('Transport - Road', 11),
    ('Transport - Other', 2),
    
    # Energy - Buildings
    ('Buildings', 6),
    
    # Energy - Fuel Production group
    ('Fuel Production - Oil and gas', 3),
    ('Fuel Production - Solid fuels', 4),
    ('Fuel Production - Other', 3),
    
    # Process group
    ('Industrial Processes - Cement', 3),
    ('Industrial Processes - Chemicals', 2),
    ('Industrial Processes - Metals', 1),
    ('Industrial Processes - Other', 4),
    
    # Agriculture group
    ('Agriculture - Livestock', 6),
    ('Agriculture - Biomass burning, soils and rice', 5),
    ('LULUCF', 7),
    
    # Waste group
    ('Waste - Solid', 2),
    ('Waste - Liquid', 2)
]

# Create color mapping that ensures adjacent related segments have similar colors
color_mapping = {
    # Energy - Power & Industry
    'Power': energy_colors[0],
    'Industry': energy_colors[1],
    
    # Energy - Transport
    'Transport - Aviation': energy_colors[2],
    'Transport - Road': energy_colors[2],
    'Transport - Other': energy_colors[2],
    
    # Energy - Buildings
    'Buildings': energy_colors[1],
    
    # Energy - Fuel Production
    'Fuel Production - Oil and gas': energy_colors[3],
    'Fuel Production - Solid fuels': energy_colors[3],
    'Fuel Production - Other': energy_colors[3],
    
    # Process
    'Industrial Processes - Cement': process_colors[0],
    'Industrial Processes - Chemicals': process_colors[1],
    'Industrial Processes - Metals': process_colors[1],
    'Industrial Processes - Other': process_colors[2],
    
    # Agriculture
    'Agriculture - Livestock': agriculture_colors[0],
    'Agriculture - Biomass burning, soils and rice': agriculture_colors[1],
    'LULUCF': agriculture_colors[2],
    
    # Waste
    'Waste - Solid': waste_colors[0],
    'Waste - Liquid': waste_colors[1]
}

# Create the figure
plt.figure(figsize=(15, 10))

# Use the ordered data
values = [x[1] for x in emissions_groups]
labels = [x[0] for x in emissions_groups]
colors_sorted = [color_mapping[x[0]] for x in emissions_groups]

# Create pie chart
wedges, texts, autotexts = plt.pie(values, 
                                  labels=labels,
                                  colors=colors_sorted,
                                  autopct='%1.1f%%',
                                  pctdistance=0.85,
                                  wedgeprops={'edgecolor': 'white',
                                            'linewidth': 1})

# Enhance text properties
plt.setp(autotexts, color='black', weight='bold', size=8)
plt.setp(texts, color='black', size=8)

# Add title
plt.title('Detailed GHG Emissions Breakdown by Sector and Subsector\nTotal: 57.1 GtCO2e in 2023', 
          pad=20, 
          color=base_colors['energy'],
          weight='bold',
          size=14)

# Add a legend
plt.legend(wedges, 
          labels,
          title="Categories",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=8)

plt.savefig('Fig5.png', 
            bbox_inches='tight',
            dpi=300,
            facecolor='white')
plt.close()