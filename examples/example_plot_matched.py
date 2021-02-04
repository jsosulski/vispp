from vispp.comparative.strips import plot_matched
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# blog_color = "#5b5d67"
# font_color = "#dddddd"
# sns.set(rc={"axes.facecolor": blog_color, "figure.facecolor": blog_color, "text.color": font_color, "axes.labelcolor": font_color, "xtick.color": font_color, "ytick.color": font_color })
sns.set_style("whitegrid")
df_ex1 = pd.read_csv("ex_1.csv")
df = pd.read_csv("classifier_benchmarks.csv")
print(df["Subject"])

# %% Naive
fig, ax = plt.subplots(1, 2, figsize=(5, 3), sharey="all")
sns.barplot(x="Classifier", y="Score", data=df_ex1, ax=ax[0])
ax[0].set_title("Bar plot")
sns.stripplot(x="Classifier", y="Score", data=df_ex1, ax=ax[1])
ax[1].set_title("Strip plot")
ax[0].set_ylim((0, 1))
fig.tight_layout()
fig.savefig("example_bar_strip.png")

plt.show()
# %%
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
ax.scatter(
    df_ex1.loc[df_ex1.Classifier == "Classifier A"].Score,
    df_ex1.loc[df_ex1.Classifier == "Classifier B"].Score,
    zorder=10,
)
ax.set_xlabel("Score Classifier A")
ax.set_ylabel("Score Classifier B")
ax.set_aspect("equal", adjustable="box")
ax.plot([0, 1], [0, 1], transform=ax.transAxes, color="k", linestyle="--")
fig.tight_layout()
fig.savefig("example_pair.png")
plt.show()
# %%
fig, ax = plt.subplots(1, 1, figsize=(5, 3))
ax, li = plot_matched(df_ex1, x="Classifier", y="Score", match_col="Subject", ax=ax)
ax.legend(li[0], li[1], title="Subject", bbox_to_anchor=(1.05, 1), loc="upper left")
fig.tight_layout()
fig.savefig("example_matched.png")
plt.show()
# %% New plot function
fig, ax = plt.subplots(1, 1, figsize=(5, 3))

x_order = ["Fancy", "SVM", "XGBoost", "Naive Bayes", "Neural Network"]

ax, leg_info = plot_matched(
    df,
    x="Classifier",
    y="Score",
    match_col="Subject",
    x_order=x_order,
    x_match_sort="Fancy",
    ax=ax,
)
ax.legend(leg_info[0], leg_info[1], title="Subject", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.set_title("Comparison of classifiers (fake data)")
fig.tight_layout()
plt.show()
