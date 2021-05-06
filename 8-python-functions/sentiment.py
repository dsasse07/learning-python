import nltk
nltk.download('vader_lexicon')
import nltk.sentiment
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
import os


def main():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  while 1 == 1:
    user_text = input('Tell me your thoughts or "exit" to quit...\n')
    if user_text == 'exit': break 
    score = get_sentiment(user_text)
    reaction = get_reaction(score)
    print(reaction)
    print("")

def get_reaction(score):
  '''
  Takes in a float score and returns a emoji as a string
  '''
  if score > 0.5:
    return '🥰'
  elif score > 0:
    return '🙂'
  elif score == 0:
    return '😶'
  elif score < -0.5:
    return '😢'
  elif score < 0:
    return '😕'

def get_sentiment(user_text):
  '''
  Takes in a user input string
  Returns a float sentiment score using nltk package
  '''
  scores = analyzer.polarity_scores(user_text)
  sentiment_score = scores['compound']
  return sentiment_score

main()
