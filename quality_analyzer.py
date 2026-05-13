#python 
import pandas as pd
import matplotlib.pyplot as plt
#Load the CSV file
df= pd.read_csv('quality_data.csv')
#show the data
print("=== Manufacturing Quality Data ===")
print(df)
print()
# Basic analysis
print("=== Process Statistics ===")
print(f"Total Batches: {len(df)}")
print(f"Average Temperature: {df['Temperature'].mean():.1f} °C")
print(f"Average Defects per Batch: {df['Defects_Found'].mean():.1f}")
print()

# Count pass/fail
pass_count = len(df[df['Status'] == 'Pass'])
fail_count = len(df[df['Status'] == 'Fail'])
print(f"Passed Batches: {pass_count}")
print(f"Failed Batches: {fail_count}")
print(f"Pass Rate: {(pass_count/len(df))*100:.1f}%")
print()
# Flag high defect batches
print("=== High Defect Alert (>5 defects) ===")
high_defects = df[df['Defects_Found'] > 5]
print(high_defects[['Batch_ID', 'Temperature', 'Defects_Found', 'Status']])
print()
# Chart 1: Defects per Batch
plt.figure(figsize=(10, 4))
colors = ['red' if s == 'Fail' else 'green' for s in df['Status']]
plt.bar(df['Batch_ID'], df['Defects_Found'], color=colors)
plt.title('Defects Found per Manufacturing Batch')
plt.xlabel('Batch ID')
plt.ylabel('Number of Defects')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('defects_chart.png')
plt.show()

# Chart 2: Temperature vs Defects
plt.figure(figsize=(6, 4))
plt.scatter(df['Temperature'], df['Defects_Found'], color='blue')
plt.title('Temperature vs Defects (Process Correlation)')
plt.xlabel('Temperature (°C)')
plt.ylabel('Defects Found')
plt.tight_layout()
plt.savefig('correlation_chart.png')
plt.show()

print("=== Charts saved successfully! ===")