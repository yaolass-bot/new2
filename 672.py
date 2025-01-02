from pydoc import text


def find_words_of_length(text,length):
  # split the text into words
  words = text.split()
# Filter words by the specified length
  words_of_length = [word for word in words if len(word) == length]
  return words_of_length

text = "Bylo prosto pasmurno, dulo s severa"
length = 4


result = find_words_of_length(text,length)
print(result)































































