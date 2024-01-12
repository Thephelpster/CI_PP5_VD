import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def page_vehicle_visualiser_body():
    st.write('##Vehicle Visualiser')
    st.info(
        '* The client is interested in having a study that visually '
        'differentiates a vehicle and non vehicle contained image.'
        )
    version = 'v1'
    if st.checkbox('Average and Variabilitiy images'):
        avg_non_vehicle = plt.imread(
            f'outputs/{version}/avg_var_non-vehicles.png')
        avg_vehicle = plt.imread(
            f'outputs/{version}/avg_var_vehicles.png')

        st.warning(
            '* We notice the average and variability images did show some '
            'general patterns where we could intuitively differentiate '
            'one from another. However, a small difference in the colour '
            'pigment of the average images is seen for both labels.'
        )

        st.image(avg_non_vehicle,
                 caption='Image without vehicle - Average and Variability')
        st.image(avg_vehicle,
                 caption='Image with vehicle - Average and Variability')