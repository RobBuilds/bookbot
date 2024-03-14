def main():
    with open('books/frankenstein.txt') as f:
      file_contents = f.read()
      print(file_contents)
      print(word_count(file_contents)," words found in the document")
      print(letter_count(file_contents))
def word_count(file_contents):
      words = file_contents.split()
      return(len(words))

def letter_count(string):
    string_dict = {}
    new_string_lower = string.lower()
    for i in new_string_lower:
      if i.isalpha():
        if i in string_dict:
          string_dict[i] += 1
        else:
          string_dict[i] = 1
    return string_dict

def sort_dict(string_dict):
    list_of_dicts = []
    for char in string_dict:
        new_dict = {"name" : char,
        "num": string_dict[char]}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(key=lambda x: x["num"], reverse=True)
    return list_of_dicts

def print_report():
    print("--- Begin report of books/frankenstein.txt ---")
    with open('books/frankenstein.txt') as f:
      file_contents = f.read()
    print(word_count(file_contents)," words found in the document")
    sorted_list = sort_dict(letter_count(file_contents))
    for dict in sorted_list:
        print(f"The '{dict['name']}' character was found {dict['num']} times")
    print("--- End report ---")
print_report()