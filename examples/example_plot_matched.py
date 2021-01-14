from vispp.comparative.strips import plot_matched
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# TODO so far marker size does not consider seaborn context
# sns.set_context('talk')
sns.set_style('whitegrid')

df = pd.read_csv("classifier_benchmarks.csv")
print(df["Subject"])
fig, ax = plt.subplots(1, 1, figsize=(5, 3))

x_order = ["LDA", "SVM", "XGBoost", "Naive Bayes", "Neural Network"]

ax, leg_info = plot_matched(
    df,
    x="Classifier",
    y="Score",
    match_col="Subject",
    x_order=x_order,
    x_match_sort="LDA",
    ax=ax,
)
ax.legend(
    leg_info[0],
    leg_info[1],
    title="Subject",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)
ax.set_title("Comparison of classifiers")
fig.tight_layout()
plt.show()
