'''
CALS301_M3_03c "Transitional Opportunities for the Transportation Sector"

PURPOSE/CONTEXT: Analyzes transportation sector's unique challenges in transitioning to low-carbon future, comparing historical transformations (like London's manure crisis) to current CO2 challenges to demonstrate potential for transformative change.

OUTLINE:

Historical transformation analogy
Current transportation emissions
Transition technologies
Integrated system solutions
Future transformation needs
CONTENT:

Late 19th century London manure crisis parallel to current CO2 challenge
Major emission sources: road vehicles, air travel, shipping
Solutions include EVs, hydrogen fuel cells, hydrogen hubs
Challenges remain in aviation and long-haul shipping
Need for integrated transit systems and smart infrastructure
Two-way modular systems potential (EVs providing grid power)
Urban planning and behavior changes required
FIGURES:

Historical comparison timeline
Transportation sector emissions breakdown
EV/hydrogen technology diagrams
Integrated transit system model
Two-way grid interaction visualization
'''
import matplotlib.pyplot as plt

# Data for emissions by source
labels = [
    "Private/Residential Road Vehicles",
    "Commercial Road Vehicles (Trucks, Delivery, etc.)",
    "Shipping",
    "Commercial Aviation",
    "Air Freight & Other Services",
    "Rail"
]

emissions = [3.87, 2.15, 1.85, 0.57, 0.35, 0.026]  # Midpoint used for shipping range
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]

# Create pie chart
plt.figure(figsize=(8, 8))
plt.pie(emissions, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Global Transportation Emissions by Source (GTCO₂e)")
plt.show()

# Data for opportunities vs. challenges by transportation category (Bar Chart)
categories = ["Road Vehicles", "Shipping", "Air", "Rail"]
opportunities = [8, 5, 3, 7]  # Opportunities ratings (out of 10, hypothetical data for illustration)
challenges = [4, 8, 9, 3]  # Challenges ratings (out of 10, hypothetical data for illustration)

x = np.arange(len(categories))  # the label locations
width = 0.35  # width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Create Bars for Opportunities and Challenges
rects1 = ax.bar(x - width/2, opportunities, width, label='Opportunities', color="#66b3ff")
rects2 = ax.bar(x + width/2, challenges, width, label='Challenges', color="#ff9999")

# Add Labels, Title, and Customize X/Y Axis
ax.set_xlabel('Transportation Categories')
ax.set_ylabel('Rating (Out of 10)')
ax.set_title('Decarbonization Opportunities vs. Challenges by Transportation Category')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Add Data Labels
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

plt.tight_layout()
plt.show()


# Data Sources:
# 1. Our World in Data - Greenhouse Gas Emissions from Transport: https://ourworldindata.org/co2-emissions-from-transport
# 2. UNEP Emissions Gap Report 2024: https://www.unep.org/resources/emissions-gap-report-2024
# 3. IEA Global Energy & CO2 Status Report 2024: https://www.iea.org/reports/global-energy-co2-status-report-2024
# 4. ICAO Global CO₂ Emissions from Aviation 2024: https://www.icao.int/environmental-protection/Pages/ClimateChange.aspx
# 5. IMO Shipping and Climate Change 2024: https://www.imo.org/en/MediaCentre/HotTopics/Pages/Reducing-greenhouse-gas-emissions-from-ships.aspx
