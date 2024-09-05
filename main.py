

def read_book(book_path):
  with open(book_path) as book:
    return book.read()

def count_words(text):
  return len(text.split())

def count_chars(text):
  char_map = {}
  for char in text:
    lower_char = char.lower()
    if lower_char in char_map:
      char_map[lower_char] += 1
    else:
      char_map[lower_char] = 1
  
  # print(char_map)
  
  return char_map
    
def sort_on(dict):
  return dict["num"]

def dict_to_sorted_list(dict):
  sorted_list = []
  for char in dict:
    sorted_list.append({"char": char, "num": dict[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def main():
  frankenstein = "./books/frankenstein.txt"

  book_text = read_book(frankenstein)
  # print(book_text)
  num_words = count_words(book_text)
  # print(f"Book contains {num_words} words")
  chars_dict = count_chars(book_text)
  chars_list = dict_to_sorted_list(chars_dict)
  
  print(f"--- Begin report of {frankenstein} ---")
  print(f"{num_words} words found in the document")
  print()
  
  for item in chars_list:
    if not item["char"].isalpha():
      continue
    
    print(f"The '{item['char']}' character was found {item['num']} times")

  print("--- End report ---")
      
  
  
if __name__ == "__main__":
  main()