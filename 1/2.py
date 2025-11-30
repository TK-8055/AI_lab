from textblob import TextBlob

print("Welcome to the Sentiment Analysis System")
print("This system evaluates text and displays polarity and subjectivity scores.\n")

user_i = input("Enter the text to analyze: ")

analysis = TextBlob(user_i)
polarity = analysis.sentiment.polarity
subjectivity = analysis.sentiment.subjectivity

if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("\n----- Sentiment Analysis Result -----")
print(f"Polarity Score     : {polarity}")
print(f"Subjectivity Score : {subjectivity}")
print(f"Overall Sentiment  : {sentiment}")

