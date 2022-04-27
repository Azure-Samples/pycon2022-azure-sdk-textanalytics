# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from flask import Flask, render_template, request
from helpers import color_code_sentiment

static_folder = os.path.abspath(
    os.path.join(
        os.path.abspath(__file__),
        "..",
        "./static",
    )
)

app = Flask(__name__, static_folder=static_folder)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def pycon_demo():
    text = request.form['text']

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    key = os.environ["AZURE_LANGUAGE_KEY"]

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    response = text_analytics_client.analyze_sentiment([text], show_opinion_mining=True)
    result = response[0]

    if result.is_error:
        return render_template("index.html", error=result.error.message)

    sentence_colored = color_code_sentiment(result.sentences)

    return render_template("index.html", overall_sentiment=result.sentiment, result=zip(sentence_colored, result.sentences))

if __name__ == '__main__':
    app.run(debug=True)