from __future__ import annotations

from dataclasses import dataclass
import pypact as pp
import os

@dataclass
class Inventory:
    """Inventory data class

    Attributes
    ----------
    times : dict[int, list[float]]
        Times in inventiry data.
    masses : dict[int, list[float]]
        Masses in inventiry data.        
    """
    times : dict[str, list[float]]
    masses : dict[str : list[float]]

    @classmethod
    def from_json(cls, json_filename : str | os.PathLike, filter : float = 0.0, normalisation : float = 1.0) -> Inventory:
        times = {}
        masses = {}
        with pp.JSONReader(json_filename) as output:
            for timestamp in output:
                time = timestamp.irradiation_time/(3600*24)
                for nuclide in timestamp.nuclides:
                    isotope = "".join([nuclide.element, str(nuclide.isotope), str(nuclide.state)])
                    mass = nuclide.grams/1000
                    if mass > filter:
                        if (isotope not in times) or (isotope not in masses):
                            times[isotope] = []
                            masses[isotope] = []
                        else:
                            times[isotope].append(time)
                            masses[isotope].append(normalisation * mass)
        return cls(times = times, masses = masses)


