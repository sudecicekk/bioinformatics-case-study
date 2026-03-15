import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("read_statistics.csv")

sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['length'], bins=30, color='skyblue', kde=True)
plt.title('Read Length Distribution')
plt.xlabel('Length (bp)')

plt.subplot(1, 3, 2)
sns.histplot(df['gc_content'], bins=30, color='olive', kde=True)
plt.title('GC Content Distribution')
plt.xlabel('GC %')

plt.subplot(1, 3, 3)
sns.histplot(df['mean_quality'], bins=30, color='gold', kde=True)
plt.title('Mean Quality Distribution')
plt.xlabel('Phred Score')

plt.tight_layout()
plt.savefig("qc_metrics_report.png")
print("Graphs saved as qc_metrics_report.png")

print("\n--- Summary Statistics ---")
print(df[['length', 'gc_content', 'mean_quality']].describe().loc[['mean', '50%']])


with open("summary_stats.txt", "w") as f:
    f.write("--- Summary Statistics ---\n")
    stats = df[['length', 'gc_content', 'mean_quality']].describe().loc[['mean', '50%']]
    f.write(stats.to_string())

print("Summary statistics saved to summary_stats.txt")