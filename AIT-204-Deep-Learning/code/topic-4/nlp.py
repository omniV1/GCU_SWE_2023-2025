 # A hand-curated word list ��� you can expand this list
POSITIVE_WORDS = {
    "good", "great", "excellent", "happy", "love", "wonderful",
    "fantastic", "amazing", "best", "enjoy", "beautiful", "nice", 
    "awesome", "incredible", "superb", "magnificent", "terrific", "outstanding"
    }

NEGATIVE_WORDS = {
      "bad", "terrible", "awful", "hate", "worst", "horrible",
      "disgusting", "poor", "sad", "boring", "ugly", "dreadful",
      "awful", "terrible", "horrible", "disgusting", "horrendous", "appalling", "abysmal", "execrable", "lamentable", "wretched", "abject", "deplorable", "shameful", "disgraceful", "repulsive", "disgusting", "horrendous", "appalling", "abysmal", "execrable", "lamentable", "wretched", "abject", "deplorable", "shameful", "disgraceful", "repulsive"
  }

# Tokenize the text into lowercase words, stripping punctuation.
# No libraries ��� just plain Python.
# Args:
#     text (str): The text to tokenize.
# Returns:
#     list: A list of lowercase words, stripped of punctuation.
def tokenize(text):
    """
    Split text into lowercase words, stripping punctuation.
    No libraries ��� just plain Python.
    """
    return [word.strip(".,!?:;") for word in text.lower().split()]

# Count the number of words in the list that are in the word list.
# Args:
#     words (list): A list of words to count.
#     word_list (set): A set of words to count against.
# Returns:
#     int: The number of words in the list that are in the word list.
def count_words(words, word_list):
    return sum(1 for word in words if word in word_list)

# Detect the sentiment of the text.
# Args:
#     text (str): The text to detect the sentiment of.
# Returns:
#     str: The sentiment of the text.
def detect_sentiment(text):
    # A very naive sentiment detector that counts positive and negative words.
    # It doesn't handle negation, sarcasm, or any of the complexities of natural language.
    # But it's a start!

    tokens = tokenize(text)
    
    pos_count = count_words(tokens, POSITIVE_WORDS)
    neg_count = count_words(tokens, NEGATIVE_WORDS)
    
    print(f"  Tokens: {tokens}")
    print(f"  Positive: {pos_count}, Negative: {neg_count}")
    
    if pos_count > neg_count:
        return "POSITIVE"
    elif neg_count > pos_count:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

# --- Test sentences ---
sentences = [
    "The movie was great and I love the story.",
    "This is the worst, most horrible film I ever saw.",
    "The food was not good at all.",
    "I don't hate it.",
    "The movie was so bad it was actually good.",
    "Fine.",
    "It was an experience.",
    "I'm not sure what to think about this.",
    "It was okay.",
    "It was great!",
    "It was terrible!",
    "It was amazing!",
    "It was horrible!",
    "It was fantastic!",
    "It was terrible!",
    "It was amazing!",
    "It was horrible!",
]

for s in sentences:
    print(f"\nText: '{s}'")
    result = detect_sentiment(s)
    print(f"  Outcome: {result}")
