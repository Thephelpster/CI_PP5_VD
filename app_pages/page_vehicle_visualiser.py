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
    st.write('### Vehicle Visualiser')
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
        
    if st.checkbox(
        'Differences between average vehicle image and non vehicle image'):
        diff_between_avgs = plt.imread(
            f'outputs/{version}/avg_diff.png')

        st.warning(
            '* This study does show some general patterns where we could '
            'intuitively differentiate between one another but that was '
            'not always the case.')
        st.image(diff_between_avgs,
                 caption='Difference between average images')
        
    if st.checkbox('Image Montage'):
        st.write('* To Refresh the montage, click on the "Create '
                 'Montage" button.')
        my_data_dir = 'inputs/vehicle-detection-image-set/data'
        labels = os.listdir(os.path.join(my_data_dir, 'validation'))
        label_to_display = st.selectbox(
            label='Select label', options=labels, index=0)
    if st.button('Create Monatage'):
        image_montage(dir_path=my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10, 25))
        
def image_montage(dir_path, label_to_display, ncols, nrows, figsize=(15, 10)):
    
    sns.set_style('white')
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(os.path.join(dir_path, label_to_display))
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f'Decrease nrows or ncols to create your montage. \n'
                f'There are {len(images_list)} in your subset. '
                f'You requested a montage with {nrows * ncols} spaces')
            return
        
        list_rows = range(0, nrows)
        list_cols = range(0,ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f'Width {img_shape[1]}px x Height {img_shape[0]}px')
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print('The label you selected doesn\'t exist.')
        print(f'The existing options are: {labels}')