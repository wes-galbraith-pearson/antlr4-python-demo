import sys
from parser.ArrayInitLexer import ArrayInitLexer
from parser.ArrayInitParser import ArrayInitParser
from unittest import TestCase
from short_to_unicode_string import ShortToUnicodeString

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.tree.Trees import Trees


def translate(input_str: str):
    input = InputStream(input_str)
    lexer = ArrayInitLexer(input=input)
    tokens = CommonTokenStream(lexer)
    parser = ArrayInitParser(tokens)
    tree = parser.init()
    walker = ParseTreeWalker() 
    walker.walk(ShortToUnicodeString(), tree)
    print('\n')

if __name__ == '__main__':
    translate(sys.argv[1])