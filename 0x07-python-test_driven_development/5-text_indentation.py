#!/usr/bin/python3
"""function that prints,text,2 new lines and these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in '.?:':
        text = text.replace(char, char + '\n\n')

    lines = [line.strip() for line in text.split('\n')]
    for line in lines:
        print(line)
