import os

import streamlit as st
from text import (
    spanish_text,
    english_text,
    spanish_labels_dictionary,
    english_labels_dictionary,
)
import pandas as pd
import altair as alt
import biome.text


st.set_page_config(page_title="Temis Demo App", layout="centered")

os.environ["TOKENIZERS_PARALLELISM"] = "False"  # To avoid warnings


def main():

    text = english_text

    # Header
    title, _, subtitle = st.beta_columns((2.3, 0.25, 0.6))

    title.title(text[0])

    subtitle.subheader(text[1])

    st.markdown("""---""")

    title, subtitle = st.beta_columns((0.4, 1))
    with title:
        language = st.select_slider(
            text[11],
            options=["English", "Spanish"],
        )

    if language == "English":
        text = english_text
        dic = english_labels_dictionary

    elif language == "Spanish":
        text = spanish_text
        dic = spanish_labels_dictionary

    st.markdown(text[2])

    st.markdown("")  # empty space

    st.header(text[3])

    st.markdown(text[4])

    st.header(text[5])

    st.markdown(f"**{text[6]}**")

    st.markdown(text[7])

    st.markdown("")  # empty space

    st.header(text[8])

    text_input = st.text_area(text[9])

    confidence_threshold = (
        0.5  # Starting value of the treshold, may be changed with the slider
    )

    pl = loading_model()  # cached function

    if text_input:

        # Making model predictions and storing them into a dataframe
        prediction = pl.predict(text_input)

        # Confidence threshold slider, changes the green categories in the graph and the categories shown
        confidence_threshold = st.slider(
            text[10],
            0,
            100,
            50,
            1,
        )

        df = pd.DataFrame(
            {
                "labels": [dic.get(pred) for pred in prediction["labels"]],
                "confidence": [s for s in prediction["probabilities"]],
                "score": [s * 100 for s in prediction["probabilities"]],
            }
        ).set_index("labels")

        # Predictions according to the threshold
        predictions = populating_predictions(df, confidence_threshold)

        df_table, _, bar_chart = st.beta_columns((1.2, 0.1, 2))

        # Class-Probabilities table
        with df_table:
            # Probabilities field
            st.dataframe(df[["score"]])

        # Class-Probabilities Chart with Confidence
        with bar_chart:
            bar_chart = bar_chart_generator(df, confidence_threshold)
            st.altair_chart(bar_chart, use_container_width=True)

        predicted_labels = predict_labels(df, confidence_threshold, 0)
        predicted_categories = predict_labels(df, confidence_threshold, 1)

        if len(predicted_categories) == 0:
            st.markdown(text[12])

        else:
            st.markdown(text[13] + ", ".join([i for i in predicted_categories]))

            if "active" or "activa" in predicted_labels:
                st.markdown(text[14])

            elif "passive" or "pasiva" in predicted_labels:
                st.markdown(text[15])

        st.header(text[16])

        st.markdown(text[17])


@st.cache(suppress_st_warning=True, allow_output_mutation=True, show_spinner=False)
def loading_model():
    """Loading of the model classifier. Passed to a function to include cache decorator"""

    return biome.text.Pipeline.from_pretrained("../models/temis_model.tar.gz")


def populating_predictions(input_df, threshold):
    """Method for getting which categories surpassed the threshold.

    Parameters
    ----------
    input_df: Pandas Dataframe
        Dataframe with predictions and score (in %)
    threshold: int
        Value from which predictions are considered valid

    Return
    ----------
    prediction_output: List[str]
        Predicted classes in descending order.
    """

    predictions_output = []
    df_sorted = input_df.sort_values(by="score")

    for index, row in df_sorted.iterrows():
        if row["score"] >= threshold * 100:
            predictions_output.append(index)

    return predictions_output


def bar_chart_generator(df, confidence_threshold):
    """Creating the bar chart, decluttering of code from main function"""

    bars = (
        alt.Chart(df.reset_index())
        .mark_bar()
        .encode(
            x=alt.X("labels", sort="-y", title=None),
            y=alt.Y("score", title=None),
            # The highlight is set based on the result
            # of the conditional statement
            color=alt.condition(
                alt.datum.score
                >= confidence_threshold,  # If the rating is >= threshold it returns True,
                alt.value("green"),  # and the matching bars are set as green.
                # and if it does not satisfy the condition
                # the color is set to steelblue.
                alt.value("steelblue"),
            ),
        )
        .mark_bar(size=20)
    )

    return bars


def predict_labels(df, confidence_threshold, mode):
    """Returning predicted labels from a dataframe given a treshold.
    mode=0 returns all labels, mode=1 returns only categories, not passive nor active"""

    predicted_labels = []

    if mode == 0:
        for i in range(len(df)):
            if df["score"][i] >= confidence_threshold:
                predicted_labels.append(df.index[i])

    elif mode == 1:
        for i in range(len(df)):
            if (
                df["score"][i] >= confidence_threshold
                and df.index[i] != "passive"
                and df.index[i] != "active"
                and df.index[i] != "pasiva"
                and df.index[i] != "activa"
            ):
                predicted_labels.append(df.index[i])

    return predicted_labels


if __name__ == "__main__":
    main()
