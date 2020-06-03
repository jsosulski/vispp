from vispp.comparative.strips import plot_matched
import pandas as pd
import matplotlib.pyplot as plt

test = pd.DataFrame({
    'classifier': ['lda', 'lda', 'svm', 'svm'],
    'score': [0.7, 0.5, 0.8, 0.9],
    'subject': [1, 2, 1, 2]
})

fig, ax = plt.subplots(1, 1, figsize=(3, 2))

plot_matched(test, x='classifier', y='score', x_order=['lda', 'svm'], match_col='subject', x_match_sort='lda', ax=ax)

plt.show()