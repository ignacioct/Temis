# Temis AMI tool

Temis is an Automatic Misogyny Identification tool. Using Deep Learning models, it can be used to predict whether a text contains misogyny, which type is it and to whom is it targetted. 

Temis, which stands for Spanish Misogyny Test (Test Español de MISoginia), was born as my bachelor's thesis in UC3M, and developed with the inmense help of [Recognai](https://www.recogn.ai). It uses Deep Neural Networks to build a classificator around datasets from AMI competitions, in several training phases. It was developed using [biome.text](https://www.recogn.ai/biome-text/) and [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) to be an open-source project, so everything from dataset sources to model weights is available.

> :warning: **Trigger Warning**: misogyny, discredit, sexual harassment, verbal harassment, active aggressions towards women.


## Dependencies
The only needed Python library to start making predictions with Temis is [*biome.text*](https://github.com/recognai/biome-text), a functional NLP library with which Temis was designed and trained. To install it, a fresh conda environment is recommended:

```shell script
conda create -n biome python~=3.7.0 pip>=20.3.0
conda activate biome
pip install biome-text==2.2.0
```

You can find more information about *biome.text* in its [Github page](https://github.com/recognai/biome-text).

## Predictions
There are five misogyny **categories**:
*   `dominance`: **Dominance**, superiority assertion of men over women, highlighting a gender inequality.
*   `derailing`: **Derailing**, justifying woman abuse by rejecting male responsibility.
*   `discredit`: **Discredit**, to cause people to stop respecting someone or believing in an ideaor person that comes from a woman with no other argument than gender.
*   `stereotype`: **Stereotype & Objectification**, widely  held  but  fixed  and  oversimplifiedimage or idea of a woman; description or comparison to narrow standards.
*   `sexual_harassment`: **Sexual Harassment & Threats of Violence**, describe  actions  as  sexual advances, requesting for sexual favours, harassment of a sexual nature, intentsto physically assert power through threats of violence.

And two **targets**:
*   `active`: targeted to an specific woman or group of women.
*   `passive`: targeted to many potential receivers, even women as genre.

A threshold of 0.5 is recommended to interpret the predictions. If any category or target surpass 0.5, it is considered to be present in the input text, and therefore it would mean it is a misogynous text. If no category nor target surpass the threshold, it considered to be a text with non-sexist content.

## API REST
The provided domain for the RESTful API is [temis.freemyip.com](temis.freemyip.com). You can these different HTTP request:

*   **/info**: offers some information about \gls{temis} and its creation, in English.
*   **/info_spanish**: offers some information about \gls{temis} and its creation, in Spanish.
*   **/label_info**: returns information about the content of the prediction, the categories, the targets and how to interpret them, in English.
*   **/label_info_spanish**: returns information about the content of the prediction, the categories, the targets and how to interpret them, in Spanish.
*   **/predict**: receives as input a parameter named text with the input text to be analyzed. Returns a list with each label and a list with the probability of each label.
*   **/predict_categories**: receives as input a parameter named text with the input text to be analyzed, and a parameter named threshold with the value of the threshold, between 0 and 1. Returns a list with each label that surpasses the given threshold. If no threshold is passed, 0.5 is used as default.
*   **/predict_binary**: receives as input a parameter named text with the input text to be analyzed, and a parameter named threshold with the value of the threshold, between 0 and 1. Returns whether the input text is misogynous or not, according to the threshold given. If no threshold is passed, 0.5 is used as default.

Here are a few examples on how to make some of the calls in the Shell and in Python:

### Bash
Curl is a utility command that is present in Linux, MacOS and Windows, and it represents the easiest way to make a HTTP Request. In the following examples, three types of calls will be showed, to show the three different scenarios (no parameters, text parameter and text and threshold parameters). 

```bash
curl -X GET https://temis.freemyip.com/info

curl -X GET "https://temis.freemyip.com/predict?text=Input%20text"

curl -X GET "https://temis.freemyip.com/predict_categories?text=Input%20text&threshold=0.7"
```

Take into consideration that the URL encoding requires the string to be in ASCII character-set, and for that reason spaces are represented as "%20". Note that, depending on how the GET request is made, spaces may be required to be changed to this format.

### Python

```python
# Import the request library
import requests

#Save the API endpoint and the call. In this example, the predict call is used
URL = "https://temis.freemyip.com/predict"

# If the call needs it, create a Python dictionary with the parammeters
PARAMS = {"text": "input text"}

# Send the request and save the response into a variable
r = requests.get(url=URL, params=PARAMS)

# Extract the json response
data = r.json()

# Take into consideration that only prediction calls return a JSON
# Info calls return an string, which can be accessed through r.content
```

## Making predictions with biome.text
You can use *biome.text* to make predictions in a Python or Jupyter script yourself with just a few lines of code:

```python 
import biome.text

pl = biome.text.Pipeline.from_pretrained("models/temis_model.tar.gz")

pl.predict("Input text")
```

## Featured models
In `models` folder all the models made for the thesis (all are explained there) can be found. Here is a quick summary:
*   `temis_model.tar.gz`: **Final Temis model**, the one with the best performance and the one intended to be used almost all times.
*   `binary_model.tar.gz`: **Binary Classification Model**, only offers a prediction of *sexist* (1) or *non-sexist* (0)
*   `multilabel_model.tar.gz`: **Multilabel Classification Model**, trained with IberEval 2018 dataset
*   `IberLEF 2021\`: folder with all models created for the **Competition Model** (*IberLEF 2021*).
*   `fine-tuned_model.tar.gz`: **Final Temis** model created with a *fine-tuning* technique instead of a full retraining phase. It performs a little bit worse, in general.

## Flask API
The REST API has been builded from a flask app, which can be also executed in local. You will need *biome.text* (previously discussed) and flask, which can be installed with:

```shell script
pip install Flask
```

To run the app, execute the following commands on your shell:
```shell script
cd flask-api
export FLASK_APP=app.py
flask run
```
As an answer prompt, Flask will respond with the localhost where the app is running. You can then make the same GET requests discussed in the REST API section, but to this local direction.

## Streamlit Demo 
An [Streamlit demo](https://github.com/streamlit/streamlit) app is included, to test out the Final Model in a more user-friendly environment. There you can send some text to predict, choose your own threshold, review results in real time and read some insight of the project. To run it you will need *biome.text* (previously discussed) and streamlit, which you can install with the following command:

```shell script
pip install streamlit
```

Once there, you can run the demo app by:
```shell script
streamlit run demo/app.py
```



