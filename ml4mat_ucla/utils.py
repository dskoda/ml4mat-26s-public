import matplotlib as mpl


def set_retina(): 
    """set retina display support in IPython notebooks
    """
    from IPython import get_ipython

    get_ipython().run_line_magic("matplotlib", "inline")
    from IPython.display import set_matplotlib_formats

    set_matplotlib_formats("retina")


def set_size(subplots=(1, 1)):
    """Set size for subplots

    Args:
        subplots (tuple, optional): number of (row,col) subplots. Defaults to (1, 1).

    Returns:
        tuple: size of subplots
    """

    fig_width_in = mpl.rcParams["figure.figsize"][0]
    fig_height_in = mpl.rcParams["figure.figsize"][1] * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


def set_dpi(dpi):
    """Set resolution for all plotted figures. Useful to create larger figures 
        on a Jupyter Notebook, or when exporting to PNG.

    Args:
        dpi (int): resolution for the figures
    """
    mpl.rcParams.update(
        {
            "figure.dpi": dpi,
        }
    )
