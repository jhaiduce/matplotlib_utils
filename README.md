# matplotlib_utils

matplotlib_utils provides functions that are useful for working with matplotlib.

## Getting started

### Prerequisites

- python 2.7
- matplotlib

### Installing

```shell
python setup.py install
```

### Functions provided

- remove_overhanging_labels: Removes any tick labels that overhang the end of the axis. This is useful when subplots have been arranged very tightly, in which case overhanging tick labels may conflict with adjacent subplots.

- add_subplot_labels: Add alphanumeric (or custom) labels to a set of Axes objects. For an array of Axes objects, label each 'a', 'b', 'c', etc. (or a specified sequence of strings).
