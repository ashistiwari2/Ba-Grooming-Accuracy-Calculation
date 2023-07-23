import pandas as pd
import streamlit as st

def calculate_accuracy_percentage(file1_path, file2_path,month):
    count=0
    # Read the CSV files into pandas DataFrames
    try:
        df1 = pd.read_csv(file1_path)
        count+=1

    except:
        st.warning("Full Length is yet to calculte. Calculate first and run this",icon="⚠️")
    try:

        df2 = pd.read_csv(file2_path)
        count+=1
    except:
        st.warning("Half Length is yet to calculte. Calculate first and run this",icon="⚠️")
    if count==2:
        # Check if both dataframes have the same column name 'Attribute'
        if  len(df1)>0 and len(df2)>0:
            appended_df = pd.concat([df1, df2])
            st.write(appended_df)
            accuracy_mean=round(appended_df['Accuracy'].mean(),3)
            st.write(f"Accuracy:{accuracy_mean}")
            st.write("Accuracy For Month {}: {:.2f}%".format(month,accuracy_mean))
            # Store accuracy in DataFrame for Month
            accuracy_df = pd.DataFrame({"Month": [month], "Accuracy": [accuracy_mean]})
                
            # Display results
            st.subheader("Accuracy Results")
            st.write(accuracy_df)

            # Convert DataFrame to CSV and store locally
            csv_file_path = f"accuracy_for_Month_{month}.csv"
            accuracy_df.to_csv(csv_file_path, index=False)
            st.success(f"Accuracy results saved to {csv_file_path}")
        else:
            if len(df1)>1:
                st.warning("Half Length is not calculated",icon="⚠️")
            elif len(df2)>1:
                st.warning("Full Length is not calculated",icon="⚠️")
            else:
                st.warning("Both Full lenth and Half length need to be calculated",icon="⚠️")

