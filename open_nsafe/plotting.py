from open_nsafe.inventory import Inventory
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def plot(inventory : Inventory, title : str, isotopes : list = [], xlim : None | list = None, ylim : None | list = None) -> Figure:
    """Inventory plotting function

    Parameters
    ----------
    inventory : Inventory
        Nucler inventory
    isotopes : list, optional
        List of isotopes to plot, by default []
    xlim : None | list, optional
        X axis limits, by default None
    ylim : None | list, optional
        Y axis limits, by default None

    Returns
    -------
    Figure
        matplotlib.figure.Figure object
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    if len(isotopes) == 0:
        isotopes = list(sorted(inventory.times.keys()))
    for isotope in isotopes:
        if isotope in inventory.times and isotope in inventory.masses:
           ax.plot(inventory.times[isotope], inventory.masses[isotope], label=isotope)
    ax.grid(which='both')
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', fontsize=16)
    if xlim is not None:
        ax.set_xlim(xlim[0], xlim[1])
    if ylim is not None:
        ax.set_ylim([ylim[0], ylim[1]])
    ax.set_title(title, fontsize=16)
    ax.set_xlabel('Time [days]', fontsize=16)
    ax.set_ylabel('Mass [kg]', fontsize=16)
    ax.tick_params(labelsize=16)
    ax.set_yscale('log')
    plt.tight_layout()
    return fig
