import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy.typing as npt
from typing import List, Union


def create_multi_bar_chart(dataframe: pd.DataFrame):
    """Create multiple bar chart with the dataframe passed

    Args:
        dataframe (pd.DataFrame): Takes a dataframe and use the index as the x axis,
        and the columns as the y axis
    """
    axs: List[Axes]

    fig, axs = plt.subplots(dataframe.columns.size)

    for idx, cal in enumerate(dataframe.columns):
        axs[idx].bar(dataframe.index, dataframe[dataframe.columns[idx]])
        axs[idx].set_title(cal)

    fig.set_size_inches(12, 6)
    fig.tight_layout()


def create_line_chart(dataframe: pd.DataFrame):
    """This function create multiple line plots in the same axes

    Args:
        dataframe (pd.DataFrame): dataframe (pd.DataFrame): Takes a dataframe and use the index as the x axis,
        and the columns as the y axis
    """

    ax: Axes

    fig, ax = plt.subplots()

    for col in dataframe.columns:
        if "population" in col:
            ax.plot(
                dataframe.index,
                dataframe[col],
                label=f"{col} x 10^7",
            )
        else:

            print(col)
            ax.plot(dataframe.index, dataframe[col], label=f"{col}")

    ax.legend()
    ax.set_xticks(list(range(0, dataframe.index.size + 1, 10)))
    ax.set_xticks(dataframe.index, minor=True)
    fig.tight_layout()
