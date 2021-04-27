# VISPP

This repository contains visualizations I use for analysis / some papers. These are the
abstract functions that should be generally applicable to any data frames. For more
in-depth explanations please refer to the respective functions.

## Installation

If you have `make` installed, setup the virtual environment using:

```
make venv
```

## Examples

There are some example scripts that plot random / fantasy data under `examples/`. Before
you run any of these please activate the virtual environment using:

```
source vispp_venv/bin/activate
```

### Comparative / Strips

The [`plot_matched`](examples/example_plot_matched.py) function can be used to create
something similar to a strips / scatter plot to compare the performance of, e.g.,
different classifiers on the same dataset, as long as the number off data points is
somewhat limited.

<img alt="Plot matched function example using fake data." src="https://user-images.githubusercontent.com/2545339/116259513-27c2f600-a776-11eb-92d2-dba51e876f8f.png" width="80%">

The added benefit of this plot function is that you can compare / track a single subject
across the classifiers. This is achieved by selecting same markers for the same data point
and a consistent x-position within one strip. Usually you want are interested mostly in
the performance in one classifier (i.e., your fancy new method). Therefore you can sort
the x-position according to the performance of your fancy new method. For example:

In this plot, within-strip position is sorted by the classification score obtained by the
_Fancy_ method. You can somewhat easily track average performance, standard deviation as
well as the classification score for each individual subject across methods.
