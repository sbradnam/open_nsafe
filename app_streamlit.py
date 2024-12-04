import os
import streamlit as st
from open_nsafe.inventory import Inventory
from open_nsafe.plotting import plot

cp = os.path.dirname(os.path.abspath(__file__))
DEMO_INVENTORY_FILE = os.path.join(cp, 'resources', 'demo_hcpb_fw.json')
PWR_INVENTORY_FILE = os.path.join(cp, 'resources', 'pwr_uo2_15.json')

def main():
    # DEMO HCPB inventory plot
    demo_inventory = Inventory.from_json(DEMO_INVENTORY_FILE)
    demo_fig = plot(demo_inventory, 'DEMO HCPB Inventory', isotopes=['U237', 'U238', 'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Am241'], ylim=[1e-8, 10])
    st.pyplot(demo_fig)
    # PWR inventory plot
    pwr_inventory = Inventory.from_json(PWR_INVENTORY_FILE)
    pwr_fig = plot(pwr_inventory, 'PWR Inventory', isotopes=['U237', 'U238', 'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Am241'], ylim=[1e-8, 10])
    st.pyplot(pwr_fig)


if __name__ == '__main__':
    main()
