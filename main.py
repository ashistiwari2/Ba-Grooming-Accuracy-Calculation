import streamlit as st
import pandas as pd
import numpy as np
import datetime
from Full_Length_code.fulllength import run_full_length
from Half_Length_Code.halflength import run_half_length_code
from accuracy_calculation.accuracycalculator import calculate_accuracy_percentage

def main():
    current_month = datetime.datetime.now().strftime("%B")
    st.title("BA Grooming  Accuracy Calculator")

    # Sidebar options
    selected_option = st.sidebar.selectbox("Choose an option", ["Half Length","Full Length","Accuracy Calculator"])

    if selected_option == "Half Length":
        run_half_length_code(current_month)
    elif selected_option =="Full Length":
        run_full_length(current_month)
    elif selected_option =="Accuracy Calculator":
        st.subheader("Accuracy Calculator for Month-{}".format(current_month))
        filename_half=f"accuracy_result_half_length_{current_month}.csv"
        filename_full=f"accuracy_result_full_length_{current_month}.csv"
        calculate_accuracy_percentage(filename_full,filename_half,current_month)
if __name__ == "__main__":
    main()
