import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("road_accident_dataset.csv")

# Columns to visualize
columns_to_plot = [
    'Visibility Level',
    'Driver Alcohol Level',
    'Driver Fatigue',
    'Emergency Response Time',
    'Traffic Volume',
    'Medical Cost',
    'Economic Loss'
]

# Set style for plots
sns.set(style="whitegrid")

# Loop through each column and create all three plots
for col in columns_to_plot:
    if df[col].dtype in ['float64', 'int64']:
        data = df[col].dropna()
        safe_col_name = col.replace(' ', '_')

        # Histogram
        plt.figure(figsize=(8, 4))
        plt.hist(data, bins=30, edgecolor='black')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(f"histogram_{safe_col_name}.png")
        plt.close()

        # Box Plot
        plt.figure(figsize=(8, 1.5))
        sns.boxplot(x=data, color="skyblue")
        plt.title(f'Box Plot of {col}')
        plt.xlabel(col)
        plt.tight_layout()
        plt.savefig(f"boxplot_{safe_col_name}.png")
        plt.close()

        # Dot Plot (Strip plot)
        plt.figure(figsize=(8, 1.5))
        sns.stripplot(x=data, color="purple", size=4, jitter=True)
        plt.title(f'Dot Plot of {col}')
        plt.xlabel(col)
        plt.tight_layout()
        plt.savefig(f"dotplot_{safe_col_name}.png")
        plt.close()
