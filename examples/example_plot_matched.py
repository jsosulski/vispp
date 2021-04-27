import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from vispp.comparative.strips import plot_matched

sns.set_style("whitegrid")
df = pd.read_csv("classifier_benchmarks.csv")
print(df["Subject"])

# %% New plot function
fig, ax = plt.subplots(1, 1, figsize=(5, 3))

x_order = ["Fancy", "SVM", "XGBoost", "Naive Bayes", "Neural Network"]

ax, leg_info = plot_matched(
    df,
    x="Classifier",
    y="Score (AUC)",
    match_col="Subject",
    x_order=x_order,
    x_match_sort="Fancy",
    ax=ax,
)
ax.legend(leg_info[0], leg_info[1], title="Subject", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.set_title("Comparison of classifiers (fake data)")
fig.tight_layout()
fig.savefig("example_fakedata.png", dpi=200)
plt.show()
