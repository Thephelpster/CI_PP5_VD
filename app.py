import streamlit as st
from app_pages.multipage import MultiPage

# loads page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_vehicle_visualiser import page_vehicle_visualiser_body
from app_pages.page_ml_performance import page_ml_performance_metrics
from app_pages.page_vehicle_detector import page_vehicle_detector_body
#from app_pages.page_project_hypothesis import page_project_hypothesis_body


# Creates an instance of the app
app = MultiPage(app_name='Vehicle Detection App')

# Add app pages here using .add_page()
app.add_page('Project Summary', page_summary_body)
app.add_page('Vehicle Visualiser', page_vehicle_visualiser_body)
app.add_page('Model Performance', page_ml_performance_metrics)
app.add_page('Vehicle Detection', page_vehicle_detector_body)
#app.add_page('Project Hypothesis', page_project_hypothesis_body)
app.run()  # Run the app
