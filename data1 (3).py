import matplotlib.pyplot as plt
import numpy as np

# Example data
categories = ['Male', 'Female', 'Non-binary']
gender_counts = [500, 600, 100]

np.random.seed(0)
ages = np.random.normal(30, 10, 1000)  # Example ages, normally distributed

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart for gender distribution
ax1.bar(categories, gender_counts, color='skyblue')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Count')
ax1.set_title('Distribution of Gender in Population')

# Histogram for age distribution
ax2.hist(ages, bins=30, edgecolor='black', alpha=0.7)
ax2.set_xlabel('Age')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Age in Population')
ax2.grid(True)

plt.tight_layout()
plt.show()
