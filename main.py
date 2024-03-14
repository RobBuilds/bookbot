def main():
    with open('books/frankenstein.txt') as f:
      file_contents = f.read()
      print(file_contents)
      print(word_count(file_contents))
      print(letter_count(file_contents))
def word_count(file_contents):
      words = file_contents.split()
      return(len(words))

def letter_count(string):
    string_dict = {}
    new_string_lower = string.lower()
    for i in new_string_lower:
      if i in string_dict:
        string_dict[i] += 1
      else:
        string_dict[i] = 1
    return string_dict
main()