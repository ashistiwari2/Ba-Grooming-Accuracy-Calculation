import streamlit as st
import pandas as pd
import numpy as np
def run_half_length_code(current_month):
    
    current_month = current_month
    st.subheader("Half Length Accuracy Calculator")
    #st.warning("Note that there shouldn't be NA-Change NA to 2 ",icon=🔥)
    st.warning("Note that there shouldn't be NA In excel(both-predicted and actual)-Change NA to 2", icon="⚠️")
    # File Upload
    actual_file = st.file_uploader("Upload Actual Half Length Excel File", type=["xlsx"])
    predicted_file = st.file_uploader("Upload Predicted Half Length Excel File", type=["xlsx"])

    if actual_file and predicted_file:
        try:
            # Read the uploaded files
            Actual = pd.read_excel(actual_file, engine='openpyxl')
            Predicted = pd.read_excel(predicted_file, engine='openpyxl')

            # Filter columns
            Actual = Actual[['Date', 'BA_ID_generated', 'BA Name', 'BA Gender', 'Region', 'BA Location', 'Attribute score',
                                'As per standards?', 'Channel', 'Blusher', 'EyeLiner', 'EyeShadow', 'Lipstick',
                                'Shaved/Groomed Beard', 'Combed Hairs', 'Image Location/Link - Whole path']]
            Predicted = Predicted[['Date', 'BA_ID_generated', 'BA Name', 'BA Gender', 'Region', 'BA Location',
                                    'Attribute score', 'As per standards?', 'Channel', 'Blusher', 'EyeLiner', 'EyeShadow',
                                    'Lipstick', 'Shaved/Groomed Beard', 'Combed Hairs', 'Image Location/Link - Whole path']]

            # Calculate accuracy
            count_Blusher = count_matching_values(Predicted, Actual, 'Blusher')
            count_EyeLiner = count_matching_values(Predicted, Actual, 'EyeLiner')
            count_EyeShadow = count_matching_values(Predicted, Actual, 'EyeShadow')
            count_Lipstick = count_matching_values(Predicted, Actual, 'Lipstick')
            count_ShavedBeard = count_matching_values(Predicted, Actual, 'Shaved/Groomed Beard')
            count_CombedHairs = count_matching_values(Predicted, Actual, 'Combed Hairs')

            total_entries = len(Predicted['BA_ID_generated'])
            Blusher_acc = round((count_Blusher / total_entries) * 100,3)
            EyeLiner_acc = round((count_EyeLiner / total_entries) * 100,3)
            EyeShadow_acc = round((count_EyeShadow / total_entries) * 100,3)
            Lipstick_acc = round((count_Lipstick / total_entries) * 100,3)
            ShavedBeard_acc = round((count_ShavedBeard / total_entries) * 100,3)
            CombedHairs_acc = round((count_CombedHairs / total_entries) * 100,3)

            # Display results
            st.subheader("Accuracy Results")
            st.write("Blusher Accuracy: {:.2f}%".format(Blusher_acc))
            st.write("EyeLiner Accuracy: {:.2f}%".format(EyeLiner_acc))
            st.write("EyeShadow Accuracy: {:.2f}%".format(EyeShadow_acc))
            st.write("Lipstick Accuracy: {:.2f}%".format(Lipstick_acc))
            st.write("Shaved/Groomed Beard Accuracy: {:.2f}%".format(ShavedBeard_acc))
            st.write("Combed Hairs Accuracy: {:.2f}%".format(CombedHairs_acc))
            # Store accuracy in DataFrame
            accuracy_df = pd.DataFrame({"Attribute": ["Blusher","Eyeliner","EyeShadow","Lipstick","Shaved/Grommed Beard","Combed Hair"], "Accuracy": [Blusher_acc,EyeLiner_acc,EyeShadow_acc,Lipstick_acc,ShavedBeard_acc,CombedHairs_acc]})
            
            # Display results
            st.subheader("Accuracy Results")
            st.write(accuracy_df)

            # Convert DataFrame to CSV and store locally
            csv_file_path = f"accuracy_result_half_length_{current_month}.csv"
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