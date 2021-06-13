from flask import Flask, request, jsonify
import biome.text

app = Flask(__name__)

# Loading the model
pl = biome.text.Pipeline.from_pretrained("../models/temis_model.tar.gz")

# Information calls
@app.route("/info", methods=["GET"])
def info_english():
    return """Temis, an Automatic Misogyny Identification tool. Created by Ignacio Talavera, June 2021.
    Temis, which stands for Spanish Misogyny Test (Test Español de MISoginia), is a bachelor's thesis in UC3M, developed with the inmense help of Recognai. 
    It uses Deep Neural Networks to build a classificator around datasets from AMI competitions. It was developed using biome.text and BETO.
    """


@app.route("/info_spanish", methods=["GET"])
def info_spanish():
    return """Temis, una herramienta de detección automática de misoginia. Creada por Ignacio Talavera, Junio 2021.
    Temis, o Test Español de MISoginia, es un Trabajo de Fin de Grado de la UC3M, desarrollado con la inmensa ayuda de Recognai.
    Diseñado sobre Redes de Neuronas Profundas, consta de un clasificador con datos de competiciones de detección de misoginia. Ha sido desarrollado usando biome.text y BETO.
    """


@app.route("/label_info", methods=["GET"])
def label_english():
    return """Temis offers three classifications. It can predict wheter an input text is misogynist or not, 
    which misogyny categories appears in the text (dominance, derailing, discredit, stereotype & objectification or sexual harassment & threats of violence)
    and to whom is it targeted (active target or passive target). With the predict call, you will receive a label list and a probabilities list. If some elements
    of the label list are above the threshold (usually 0.5), these label are predicted for the text, and therefore it is considered to be misogynistic."""


@app.route("/label_info_spanish", methods=["GET"])
def label_spanish():
    return """Temis ofrece tres clasificaciones. Puede predecir si un texto de entrada es misógino o no, 
    qué tipo de misoginia presenta (dominancia, descarrilamiento, desacreditación, estereotipo & objetificación o acoso sexual & amenazas de violencia)
    y a quién está destinado (objetivo activo o pasivo). Con una llamada 'predict', se enviará como respuesta una lista de categorias y una lista de probabilidades.
    Si alguna de las categorias tiene una probabilidad asociada mayor a un valor umbral (normalmente 0.5), se considera que esas categorias están presentes en el texto
    y que, por tanto, es un texto misógino.
    """


@app.route("/predict", methods=["GET"])
def predict():

    # Checking the existence of a text field
    if "text" not in request.args:
        return jsonify(
            {
                "error": """Please, send a GET request with the following JSON as input: {text: your input text}"""
            }
        )

    # Checking the length of the text field
    if len(request.args["text"]) > 280:
        return jsonify(
            {
                "error": "The length of the input text cannot be greater than 280 characters"
            }
        )

    return jsonify(
        {"text": request.args["text"], "predictions": pl.predict(request.args["text"])}
    )


# Obtaining text and threshold as input, returning only labels above the threshold
@app.route("/predict_categories", methods=["GET"])
def predict_categories():

    # Checking the existence of a text field
    if "text" not in request.args:
        return jsonify(
            {
                "error": """Please, send a GET request with the following JSON as input: {text: your input text, threshold: your threshold}. If no threshold is passed, 0.5 will be the assigned value."""
            }
        )

    # Checking the existence of a threshold field
    if "threshold" not in request.args:
        threshold = 0.5
    else:
        threshold = float(request.args["threshold"])

    # Checking the length of the text field
    if len(request.args["text"]) > 280:
        return jsonify(
            {
                "error": "The length of the input text cannot be greater than 280 characters"
            }
        )

    # Make the prediction
    predictions = pl.predict(request.args["text"])

    # Obtain list of labels that surpass the threshold
    output = []
    for i in range(len(predictions)):
        if float(predictions["probabilities"][i]) >= threshold:
            output.append(predictions["labels"][i])

    if output == []:
        output = "non-misogynistic"

    return jsonify(
        {"text": request.args["text"], "treshold": threshold, "predictions": output}
    )


# Obtaining text and threshold as input, returning True is any label surpass the threshold
@app.route("/predict_binary", methods=["GET"])
def predict_binary():

    # Checking the existence of a text field
    if "text" not in request.args:

        return jsonify(
            {
                "error": """Please, send a GET request with the following JSON as input: {text: your input text, threshold: your threshold}. If no threshold is passed, 0.5 will be the assigned value."""
            }
        )
    # Checking the existence of a threshold field
    if "threshold" not in request.args:
        threshold = 0.5
    else:
        threshold = float(request.args["threshold"])

    # Checking the length of the text field
    if len(request.args["text"]) > 280:
        return jsonify(
            {
                "error": "The length of the input text cannot be greater than 280 characters"
            }
        )

    # Make the prediction
    predictions = pl.predict(request.args["text"])

    # Obtain if any label surpass the threshold
    output = "non-misogynistic"

    for i in range(len(predictions)):
        if float(predictions["probabilities"][i]) >= threshold:
            output = "misogynistic"

    return jsonify(
        {"text": request.args["text"], "treshold": threshold, "prediction": output}
    )
