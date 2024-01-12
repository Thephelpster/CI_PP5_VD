import streamlit as st


def page_summary_body():

    st.write('### Quick Project Summary')

    st.info(
        "Vehicle Detection App is a machine learning project thats goal is to be able to "
        "differentiate between images that contain a vehicle and those that do not. "
        "This project utilises Streamlit Dashboard and gives the cilent the ability to "
        "upload an image in order to quickly check if it contains a vehicle. The results "
        "are then shown in the dashboard along with projects hypothesis and details about "
        "the performance of the model."
    )

    st.success(
        "Vehicle Detector App has two business requirements:\n"
        "1. The client would like to have a study of the dataset collected \n"
        "2. The client would like to have an ML model developed in order "
        "to be able to indentify vehicles in images."
    )
    
    st.write(
        "* For more detailed information on the project, please read the [README file]"
        "(https://github.com/Thephelpster/CI_PP5_VD)."
    )