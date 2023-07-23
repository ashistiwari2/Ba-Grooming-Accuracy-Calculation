import os
import streamlit as st
def remove():
    st.subheader("Exisiting File removal from Server")
    # Directory where the CSV files are located
    directory_path = './'

    # Get a list of files in the directory
    file_list = os.listdir(directory_path)
    #print(file_list)
    dynamic_content=[]
    # Iterate through the files and remove files with the CSV extension
    for filename in file_list:
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            print(file_path)
            dynamic_content.append(file_path)
    if len(dynamic_content)<1:
        st.warning("No file in server yet",icon="🤖")
    else:
    
        
                # Create a dropdown menu using st.selectbox()
        selected_option = st.selectbox('Select File to delete:', dynamic_content)
        st.write('You selected:', selected_option)
        # if st.checkbox("You want to delete selected file"):
        #     os.remove(file_path)
        #     st.success("{} removed successfully".format(selected_option))
        #     # Create a checkbox
        checked = st.checkbox('You want to delete selected file', key='my_checkbox')

    # Perform your action (e.g., based on a user input or event)
        if checked:
                    
            os.remove(file_path)
            st.success("{} removed successfully".format(selected_option))
            # Your operation code here

            # Execute JavaScript to uncheck the checkbox after performing the action
            st.markdown("""
                <script>
                document.querySelector("input[data-testid='stSession-my_checkbox']").checked = false;
                </script>
            """, unsafe_allow_html=True)

#         os.remove(file_path)
#         print(f"File {filename} has been deleted.")
