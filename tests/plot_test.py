import os
import pytest
from open_nsafe.inventory import Inventory
from open_nsafe.plotting import plot

cp = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(cp, '..', 'resources', 'demo_hcpb_fw.json')
INVENTORY = Inventory.from_json(INVENTORY_FILE)

class TestPlot:
    def test_plot_with_isotopes_and_limits(self):
        fig = plot(INVENTORY, 'Test Inventory', isotopes=['U237', 'U238', 'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Am241'], ylim=[1e-8, 10])
        assert True

    def test_default_plot(self):
        fig = plot(INVENTORY, 'Test Inventory')
        assert True

    def test_plot_with_limits(self):
        fig = plot(INVENTORY, 'Test Inventory', xlim=[0.0, 2000.0], ylim=[1e-8, 10])
        assert True
    

    def test_plot_with_isotopes(self):
        fig = plot(INVENTORY, 'Test Inventory', isotopes=['U237', 'U238', 'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Am241'])
        assert True
    

    