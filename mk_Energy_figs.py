import matplotlib.pyplot as plt
import numpy as np

# Define the official color palette
colors = {
    'carnelian': '#B31B1B',
    'carnelian_light': '#D94F4F',
    'ec_black': '#393F47',
    'light_gray': '#ECECEC',
    'dark_gray': '#A7A8AA',
    'white': '#FFFFFF',
    'hyperlink': '#3A708B',
    'sky_blue': '#92B2C4',
    'sea_blue': '#ACE1E5',
    'seaweed': '#52B7AB',
    'money': '#8DC440',
    'gold': '#FBB040'
}

# Data for all four charts
emissions_by_source = {
    'Fossil CO2': 39.0,
    'CH4 (Methane)': 9.8,
    'LULUCF CO2': 4.0,
    'N2O': 2.6,
    'F-gases': 1.7
}

total_GHG = sum(emissions_by_source.values())

sector_percentages = {
    'Power': 26,
    'Industry': 11,
    'Transport': 15,
    'Buildings': 6,
    'Fuel Production': 10,
    'Industrial Processes': 10,
    'Agriculture': 11,
    'LULUCF': 7,
    'Waste & Other': 4
}

emissions_by_sector = {k: (v/100)*total_GHG for k, v in sector_percentages.items()}

industry_breakdown = {
    'Chemicals': 2.3,
    'Metals': 1.7,
    'Cement': 2.3
}

transport_breakdown = {
    'Aviation': 1.1,
    'Road': 6.3,
    'Other Transport': 1.1
}

# Common plotting parameters
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelweight'] = 'bold'

def create_pie_chart(data, title, filename, color_sequence):
    plt.figure(figsize=(12, 8))
    
    # Create pie chart
    values = list(data.values())
    total = sum(values)
    
    # Sort wedges from largest to smallest for better visual hierarchy
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    values = [x[1] for x in sorted_data]
    labels = [f'{x[0]}\n({x[1]:.1f} GtCO2e)' for x in sorted_data]
    
    # Create pie with a slight explosion effect on the largest segment
    explode = [0.05] + [0] * (len(values)-1)
    
    wedges, texts, autotexts = plt.pie(values, 
                                      explode=explode,
                                      labels=labels,
                                      colors=color_sequence,
                                      autopct='%1.1f%%',
                                      pctdistance=0.85,
                                      wedgeprops={'edgecolor': colors['white'],
                                                'linewidth': 2})
    
    # Enhance text properties for better readability
    plt.setp(autotexts, color=colors['ec_black'], weight='bold', size=10)
    plt.setp(texts, color=colors['ec_black'], size=12)
    
    # Add title with total
    plt.title(f'{title}\nTotal: {total:.1f} GtCO2e', 
              pad=20, 
              color=colors['carnelian_light'],
              weight='bold',
              size=14)
    
    # Add a legend
    plt.legend(wedges, 
              [x[0] for x in sorted_data],
              title="Categories",
              loc="upper right",
              bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.savefig(filename, 
                bbox_inches='tight',
                dpi=300,
                facecolor=colors['white'])
    plt.close()

# Figure 1: Total GHG Emissions Breakdown
create_pie_chart(
    emissions_by_source,
    'Total GHG Emissions Breakdown',
    'Fig1.png',
    [colors['carnelian_light'], colors['hyperlink'], colors['seaweed'], 
     colors['money'], colors['gold']]
)

# Figure 2: Emissions by Sector
create_pie_chart(
    emissions_by_sector,
    'Emissions by Sector',
    'Fig2.png',
    [colors['hyperlink'], colors['sea_blue'], colors['seaweed'], 
     colors['sky_blue'], colors['money'], colors['gold'],
     colors['carnelian_light'], colors['dark_gray'], colors['light_gray']]
)

# Figure 3: Industry Breakdown
create_pie_chart(
    industry_breakdown,
    'Industry Sector Breakdown',
    'Fig3.png',
    [colors['hyperlink'], colors['seaweed'], colors['money']]
)

# Figure 4: Transport Breakdown
create_pie_chart(
    transport_breakdown,
    'Transport Sector Breakdown',
    'Fig4.png',
    [colors['carnelian_light'], colors['hyperlink'], colors['seaweed']]
)