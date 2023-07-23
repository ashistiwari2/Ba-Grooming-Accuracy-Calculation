import os
import pandas as pd

import streamlit as st
def run_full_length(current_month):
    current_month = current_month
    st.subheader("Full Length Accuracy Calculator")
    #st.warning("Note that there shouldn't be NA-Change NA to 2 ",icon=🔥)
    st.warning("Note that there shouldn't be NA In excel(both-predicted and actual)-Change NA to 2", icon="⚠️")
    # File Upload
    actual_file = st.file_uploader("Upload Actual Full Length Excel File", type=["xlsx"])
    predicted_file = st.file_uploader("Upload Predicted Full Length Excel File", type=["xlsx"])
    if actual_file and predicted_file:
        try:
            Actual = pd.read_excel(actual_file, engine='openpyxl')
            Predicted = pd.read_excel(predicted_file, engine='openpyxl')
            # Calculate accuracy
            count_uniform = count_matching_values(Predicted, Actual, 'Uniform')
            count_shoes = count_matching_values(Predicted, Actual, 'Shoes')
            total_entries = len(Predicted['BA_ID_generated'])
            Uniform_acc = round((count_uniform / total_entries) * 100,3)
            Shoes_acc = round((count_shoes / total_entries) * 100,3)
            # Display results
            st.subheader("Accuracy Results")
            st.write("Uniform Accuracy: {:.2f}%".format(Uniform_acc))
            st.write("Shoes Accuracy: {:.2f}%".format(Shoes_acc))
            # Store accuracy in DataFrame
            accuracy_df = pd.DataFrame({"Attribute": ["Shoes","Unifrom"], "Accuracy": [Shoes_acc,Uniform_acc]})
            
            # Display results
            st.subheader("Accuracy Results")
            st.write(accuracy_df)

            # Convert DataFrame to CSV and store locally
            csv_file_path = f"accuracy_result_full_length_{current_month}.csv"
            accuracy_df.to_csv(csv_file_path, index=False)
            st.success(f"Accuracy results saved to {csv_file_path}")
        except Exception as e:
            st.warning(e,icon="🚨")
def count_matching_values(predicted_df, actual_df, column):
    count = 0
    for i in range(len(predicted_df['BA_ID_generated'])):
        if predicted_df[column][i] == actual_df[column][i]:
            count += 1
    return count


