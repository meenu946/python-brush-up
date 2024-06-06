def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    char_count = len(text.replace(" ", ""))
    
    word_freq = {}
    for word in words:
        word = word.lower()  
        word_freq[word] = word_freq.get(word, 0) + 1
    
    most_frequent_word = max(word_freq, key=word_freq.get)
    
    analysis_results = {
        "word_count": word_count,
        "char_count": char_count,
        "most_frequent_word": most_frequent_word
    }
    
    return analysis_results

text = "This is a test text. This text contains some words. Words are repeated in this text."
analysis = analyze_text(text)
print("Analysis results:")
print("Word count:", analysis["word_count"])
print("Character count (excluding whitespaces):", analysis["char_count"])
print("Most frequent word:", analysis["most_frequent_word"])

