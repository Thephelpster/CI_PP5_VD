import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/sets_distribution_pie.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.write("### Model History")

    model_acc = plt.imread(
        f"outputs/{version}/model_training_acc.png")
    st.image(model_acc, caption='Model Training Accuracy')

    model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Losses', 'Accuracy']))
    st.write("---")

    st.write("### Confusion Matrix")
    model_acc = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_acc, caption='Confusion Matrix')
    st.write("---")