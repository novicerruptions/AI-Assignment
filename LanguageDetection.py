# 2. Write a python program to identify a language.

# Solution: To identify the language of a given text, we can use a Python library called langdetect. 

from langdetect import detect

def identify_language(text):
    try:
        lang = detect(text)
        return lang
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example usage
text = "Hello, how are you?"

language = identify_language(text)

if language:
    print(f"The language of the text is: {language}")
else:
    print("Language detection failed.")


# In this program, the identify_language function takes a text parameter and uses the detect function from langdetect to detect the language of the given text. It returns the detected 
# language as a string.

# The program provides an example usage where the text variable contains the input text to identify the language. It calls the identify_language function and prints the detected language 
# if it's successful, or prints an error message if language detection fails.
