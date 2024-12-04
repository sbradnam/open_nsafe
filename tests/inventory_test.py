import os
import pytest
from open_nsafe.inventory import Inventory

cp = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(cp, '..', 'resources', 'demo_hcpb_fw.json')

class TestInventory:
    def test_from_json(self):
        inventory = Inventory.from_json(INVENTORY_FILE)
        assert len(inventory.times) == len(inventory.masses)
        assert len(inventory.times['U239']) == len(inventory.masses['U239'])
        assert inventory.times['U239'][0] == pytest.approx(60.875)
        assert inventory.masses['U239'][-1] == pytest.approx(4.59702956595431e-06)