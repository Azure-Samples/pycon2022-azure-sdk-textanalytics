# Sentiment Analysis and Opinion Mining with the Azure Text Analytics Client Library

This demo showcases the sentiment analysis and opinion mining feature of the Azure Cognitive Language service using the Text Analyics client library for Python.

![image](https://user-images.githubusercontent.com/31998003/165418390-1045c654-cb64-452b-9a48-cdece73b0ce3.png)

## Features

Sentiment analysis and opinion mining are features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. These features help you find out what people think of your brand or topic by mining text for clues about positive or negative sentiment, and can associate them with specific aspects of the text.

See more about sentiment analysis and opinion mining in the [product documentation](https://docs.microsoft.com/azure/cognitive-services/language-service/sentiment-opinion-mining/how-to/call-api).

## Getting Started

### Prerequisites

- Python 3.6 later
- An [Azure subscription](https://azure.microsoft.com/free/) and a
  [Language resource](https://docs.microsoft.com/azure/cognitive-services/cognitive-services-apis-create-account?tabs=language%2Cwindows#create-a-new-azure-cognitive-services-resource) to run this demo.

### Installation

This demo requires the [azure-ai-textanalytics](https://pypi.org/project/azure-ai-textanalytics/) client library and [flask](https://pypi.org/project/Flask/).

`pip install azure-ai-textanalytics flask`

### Quickstart

1. `git clone https://github.com/Azure-Samples/pycon2022-azure-sdk-textanalytics.git`
2. `cd pycon2022-azure-sdk-textanalytics`


## Demo

1. Set your Language endpoint and API key values to the following environment variables:

    `AZURE_LANGUAGE_ENDPOINT`

    `AZURE_LANGUAGE_KEY`

2. Run `python app.py` and open the browser on `http://127.0.0.1:5000/`.


### Resources

Discover more with the Azure Text Analytics client library:

[PyPi](https://pypi.org/project/azure-ai-textanalytics/) | [Conda](https://anaconda.org/microsoft/azure-ai-textanalytics) | [Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples)
  