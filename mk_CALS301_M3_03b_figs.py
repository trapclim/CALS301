import matplotlib.pyplot as plt
import numpy as np

# FIGURE 1: Pie Chart of Global Emissions by Source
def fig1_pie_chart():
    labels = [
        "Coal", 
        "Natural Gas", 
        "Cement", 
        "Steel", 
        "Other Renewables"
    ]
    emissions = [8.4, 5.5, 1.7, 2.5, 2.0]  # GTCO₂e annually (example data)
    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
    
    plt.figure(figsize=(8, 6))
    plt.pie(emissions, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title("Fig 1: Global Emissions by Source (GTCO₂e)")
    plt.show()


# FIGURE 2: Bar Chart Comparing Reduction Potential Across Renewables
def fig2_bar_chart():
    categories = ["Wind", "Solar", "Geothermal", "Hydro"]
    reduction_potential = [8.1, 6.5, 1.3, 10.0]  # Hypothetical % reduction potential
    
    colors = ["#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
    x = np.arange(len(categories))
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, reduction_potential, color=colors, alpha=0.8)
    plt.title("Fig 2: Emissions Reduction Potential Across Renewables")
    plt.xlabel("Renewable Types")
    plt.ylabel("Potential Reduction (% of Global Emissions)")
    plt.xticks(x, categories)
    for i, value in enumerate(reduction_potential):
        plt.text(i, value + 0.5, f"{value}%", ha='center')
    plt.show()


# FIGURE 3: CCUS Process for Cement and Steel (Schematic)
def fig3_ccus_schematic():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Draw the flowchart elements
    ax.add_patch(plt.Rectangle((0, 0.5), 1, 0.5, color="#66b3ff", alpha=0.6, label="Cement Factory"))
    ax.add_patch(plt.Rectangle((0, -0.5), 1, 0.5, color="#ff9999", alpha=0.6, label="Steel Factory"))
    ax.add_patch(plt.Rectangle((2, 0), 2, 0.5, color="#99ff99", alpha=0.6, label="Carbon Capture Block"))
    ax.add_patch(plt.Rectangle((5, 0), 2, 0.5, color="#c2c2f0", alpha=0.6, label="Storage Facility"))
    
    # Add arrows
    ax.annotate("", xy=(1, 0.75), xytext=(2, 0.25), arrowprops=dict(facecolor="black", width=1.5))
    ax.annotate("", xy=(1, 0.25), xytext=(2, 0.25), arrowprops=dict(facecolor="black", width=1.5))
    ax.annotate("", xy=(4, 0.25), xytext=(5, 0.25), arrowprops=dict(facecolor="black", width=1.5))
    
    # Add text descriptions
    ax.text(0.5, 0.75, "Cement Plant", ha="center", va="center", fontsize=10)
    ax.text(0.5, 0.25, "Steel Plant", ha="center", va="center", fontsize=10)
    ax.text(3, 0.25, "CO2 Captured", ha="center", va="center", fontsize=10)
    ax.text(6, 0.25, "Long-term Storage", ha="center", va="center", fontsize=10)
    
    # Remove axes for visual focus
    ax.axis("off")
    plt.title("Fig 3: CCUS Process for Cement and Steel", fontsize=14)
    plt.legend(loc="lower right")
    plt.show()

# Call the functions to display the figures
fig1_pie_chart()
fig2_bar_chart()
fig3_ccus_schematic()
