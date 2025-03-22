```
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
```
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
