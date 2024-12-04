import os
import streamlit as st
from open_nsafe.inventory import Inventory
from open_nsafe.plotting import plot

cp = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(cp, 'resources')

def main():
    files = [file for file in os.listdir(RESOURCES) if file.endswith('.json')]
    spectrum_normalisation = st.number_input('Enter target mass in kg')
    spectrum_file = st.selectbox('Pick a spectrum', files)
    spectrum_path = os.path.join(RESOURCES, spectrum_file)
    inventory = Inventory.from_json(spectrum_path, normalisation=spectrum_normalisation)
    isotope_list = inventory.masses.keys()
    isotopes = st.multiselect('Select isotopes', isotope_list)
    fig = plot(inventory, spectrum_file, isotopes=isotopes)
    st.pyplot(fig)


if __name__ == '__main__':
    main()
