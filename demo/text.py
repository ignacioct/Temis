english_text = [
    """Temis Demo App""",
    """An app by [@ignacioct](https://github.com/ignacioct)""",
    """Hey there, welcome! This demo app introduces Temis, an Automatic Misogyny Detection tool for
    Spanish written text. You will learn about the project, make some predictions and see how to implement
    Temis in any other system.""",
    "What's Temis?",
    """Temis, which stands for Spanish Misogyny Test (Test Español de MISoginia), was born as my bachelor's thesis
    in UC3M, and developed with the inmense help of [Recognai](https://www.recogn.ai). It uses Deep Neural Networks 
    to build a classificator around datasets from AMI competitions, in several training phases. It was developed using 
    [biome.text](https://www.recogn.ai/biome-text/) and [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) to
    be an open-source project, so everything from dataset sources to model weights is available.""",
    "Disclaimer",
    """TW: misogyny, discredit, sexual harassment, verbal harassment, active aggressions towards women.""",
    """This model has been trained over data with real misogyny in it, covering categories such as discredit, sexual harassment, 
    dominance, derailing, and active aggressions to collective and individual women. Example text will be as light-weighted as 
    possible, but care is advised to use or study Temis, specially with sensitive people.""",
    "Let's make some predictions",
    """For example: *¡Las mujeres a la cocina!*""",
    """We can select a threshold to decide which confidence must be obtained to consider it a prediction.""",
    "Choose a language",
    "The input message has not been classified as misogynistic with the given threshold",
    "The input message has been classified as misogynistic, over the following categories: ",
    "The misogyny in the message has been also classified as active: against a particular woman or group of women",
    "The misogyny in the message has been also classified as passive: against a large colective of women or against all women",
    "How the multilabel model work?",
    """Usually, classifier models are train to place something into one of some categories. This problem could have been approached with
    three different classifiers: one to tell if there's misogyny or not, one for the category (discredit, dominance ...) and one for the target 
    (active or passive). We choosed a somehow different, but similar approach. Instead of trying to figure it a label for a given input, we let the 
    model predict the probabilities of each label, and if they surpass a given threshold (usually 50% confidence), they are taken as predicted. So, 
    if any category or target is predicted, we suppouse there is misogyny in the text, and then the categories and targets with the highest 
    probabilities are the ones that the model thinks that are most likely to be happening in the text. More than one category could be predicted, 
    but that's okay too. Language is ambiguous after all, maybe more than one type is taking place in the text, with with different levels of presence.""",
]

spanish_text = [
    """Temis Demo App""",
    """Una app hecha por [@ignacioct](https://github.com/ignacioct)""",
    """¡Hola! Bienvenida. Esta aplicación demo sirve para presentar Temis, una herramienta de detección 
    automática de misoginia en texto escrito español. Aqui podras aprender acerca de este proyecto, hacer 
    algunas preddiciones y ver cómo implementar Temis en cualquier otro sistema.""",
    "¿Qué es Temis?",
    """Temis, o Test Español de MISoginia, es un proyecto nacido como Trabajo de Fin de Grado en la UC3M que 
    ha sido desarrollado con la inmensa ayuda de [Recognai](https://www.recogn.ai). Emplea redes de neuronas 
    profundas para construir un clasificador entrenado sobre sets de datos de competiciones de detección de 
    misoginia, con varias fases de entrenamiento. Ha sido desarrollado con [biome.text](https://www.recogn.ai/biome-text/) 
    and [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) desde un enfoque *open-source*, por 
    lo que todo está disponible online, desde los sets de datos hasta los pesos de los modelos.""",
    "Aviso",
    "TW: misoninia, desacreditación verbal, acoso sexual, abuso verbal y agresiones activas contra mujeres",
    """Este modelo ha sido entrenado sobre datos con misoginia real, cubriendose categorias como desacreditación, acoso sexual, 
    dominancia, abuso verbal y agresiones activas contra mujeres individuales y colectivos. Los textos de ejemplo intentan ser 
    todo lo ligeros y anecdóticos posibles, pero se pide cuidado al usar o estudiar Temis, sobre todo para personas sensibles.""",
    "Hagamos algunas prediciones",
    "Por ejemplo: *¡Las mujeres a la cocina!*",
    "Podemos seleccionar un intervalo de confianza a partir del cual considerar las predicciones válidas.",
    "Selecciona un idioma",
    "El mensaje introducido no ha sido clasificado como misógino, dado el intervalo de confianza",
    "El mensaje ha sido clasificado como misógino sobre las siguientes categorias: ",
    "El mensaje ha sido también clasificado como misoginia activa: contra una mujer o un grupo de mujeres en particular",
    "El mensaje ha sido también clasificado como misoginia pasiva: contra un colectivo de mujeres o contra toda las mujeres",
    "¿Cómo funciona un modelo multilabel",
    """Normalmente, los modelos clasificadores son entrenados para categorizar una entrada dentro de una categoria. El sistema podría 
    haber sido diseñado como tres clasificadores diferentes: uno para comprobar si hay misoginia en el texto, otro para predecir la categoria 
    (dominancia, desacreditación ...) y el último para buscar el objetivo (activo o pasivo). En Temis se ha utilizado una aproximación diferente, 
    pero también similar. En lugar de intentar predecir una categoria para un input, dejamos que el modelo prediga las probabilidades (o la confianza) 
    de cada categoria, y si estas probabilidades superan un intervalo de confianza (normalmente un 50%), son tomadas como categorias predecidas. Por 
    lo tanto, si alguna categoria u objetivo superan ese valor, se supone que el modelo ha considerado que hay misoginia en el text, y las categorias y objetivos 
    con las mayores probabilidades son las que el modelo considera que es más probable que esten ocurriendo en el texto. Más de una categoria puede ser predecida, 
    y eso también está bien. El lenguaje es ambiguo, y más de un tipo puede pasar en el texto, pero con diferente intensidad o presencia.""",
]

english_labels_dictionary = {
    "passive": "passive",
    "active": "active",
    "discredit": "discredit",
    "stereotype": "stereotype",
    "derailing": "derailing",
    "sexual_harassment": "sexual harassment",
    "dominance": "dominance",
}

spanish_labels_dictionary = {
    "passive": "pasiva",
    "active": "activa",
    "discredit": "desacreditación",
    "stereotype": "estereotipo",
    "derailing": "descarrilamiento",
    "sexual_harassment": "acoso sexual",
    "dominance": "dominancia",
}
