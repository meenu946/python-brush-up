def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    reversed_text = ' '.join(reversed_words)
    return reversed_text

example_text = "Hello world this is a test"
reversed_text = reverse_words(example_text)
print(f"Original text: {example_text}")
print(f"Reversed words: {reversed_text}")