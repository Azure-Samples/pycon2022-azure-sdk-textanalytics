# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

def wrap_text_in_color(curr_sentence, sentiment_obj, replace_map):
    text = sentiment_obj.text
    key = len(replace_map)
    replace_map[f">{key}<"] = text
    if sentiment_obj.sentiment == "negative":
        return curr_sentence.replace(text, f"<mark class='red'>>{key}<</mark>", 1)
    elif sentiment_obj.sentiment == "positive":
        return curr_sentence.replace(text, f"<mark class='green'>>{key}<</mark>", 1)
    elif sentiment_obj.sentiment in ["neutral", "mixed"]:
        return curr_sentence.replace(text, f"<mark class='purple'>>{key}<</mark>", 1)
    return curr_sentence


def color_code_sentiment(sentences):
    sentiment = []
    replace_mapping = {}
    for sentence in sentences:
        curr_sentence = sentence.text
        for opinion in sentence.mined_opinions:
            curr_sentence = wrap_text_in_color(curr_sentence, opinion.target, replace_mapping)
            for assessment in opinion.assessments:
                curr_sentence = wrap_text_in_color(curr_sentence, assessment, replace_mapping)
        sentiment.append(curr_sentence)

    sentences = ["".join(sentence) for sentence in sentiment]
    result = []
    for sentence in sentences:
        for key, val in replace_mapping.items():
            if sentence.find(key) != -1:
                sentence = sentence.replace(key, val)
        result.append(sentence)
    return result
