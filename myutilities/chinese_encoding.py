"""
This code works with python3.x
"""

# coding=utf-8

import sys

class wordToEncode:
    """Decode the words"""

    def __init__(self, wordin):
        self.wordin = wordin

    def to_unicode(self):
        word = self.wordin
        return word.encode('ascii')

if __name__ == '__main__':
   
    inputs = "你好，世界！" 
    test = wordToEncode(inputs)
    print(inputs)
    print(test.to_unicode())
