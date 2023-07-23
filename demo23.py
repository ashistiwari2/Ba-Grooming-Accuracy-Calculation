import pandas as pd
# Read the CSV files into pandas DataFrames
df1 = pd.read_csv('accuracy_result_full_length_July.csv')
df2 = pd.read_csv('accuracy_result_half_length_July.csv')
print(df1)
print(df2)

# Merge the two dataframes based on the common column ('Attribute' in this case)
appended_df = pd.concat([df1, df2])

# Now, the merged_df will contain the combined data from both CSV files with the same 'Attribute' column
print(appended_df)