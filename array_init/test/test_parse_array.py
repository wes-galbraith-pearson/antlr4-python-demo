from parser.ArrayInitLexer import ArrayInitLexer
from parser.ArrayInitParser import ArrayInitParser
from unittest import TestCase

from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Trees import Trees


class TestParseArray(TestCase):
    def test_parse_array(self):
        input = InputStream("{1,2,3}")
        lexer = ArrayInitLexer(input=input)
        tokens = CommonTokenStream(lexer)
        parser = ArrayInitParser(tokens)
        tree = parser.init()
        tree_str = Trees.toStringTree(tree, None, parser).replace(" ", "")
        expected_tree = "(init {(value 1),(value 2),(value 3)})".replace(
            " ", ""
        )
        self.assertEqual(
            tree_str,
            expected_tree,
            msg=f"Expected\n\t{expected_tree}\n, but found\n\t{tree_str}",
        )

    def test_parse_nested_array(self):
        input = InputStream("{1, {2,3}, 4}")
        lexer = ArrayInitLexer(input=input)
        tokens = CommonTokenStream(lexer)
        parser = ArrayInitParser(tokens)
        tree = parser.init()
        tree_str = Trees.toStringTree(tree, None, parser).replace(" ", "")
        expected_tree = "(init {(value 1), (value (init {(value 2), (value 3)})), (value 4)})".replace(
            " ", ""
        )
        self.assertEqual(
            tree_str,
            expected_tree,
            msg=f"Expected\n\t{expected_tree}\n, but found\n\t{tree_str}",
        )
