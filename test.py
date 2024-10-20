import tree_sitter_python
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tree_sitter_python.language())

parser = Parser(PY_LANGUAGE)
