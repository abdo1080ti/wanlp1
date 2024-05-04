from transformers import pipeline

classifier = pipeline("sentiment-analysis")

#text = "انا اكره هذا الفلم انه ممل جدا."

def sent_analysis(text):
    result = classifier(text)
    return result[0]['label']