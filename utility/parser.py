# A set of parsing utilities using tree-sitter

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

COMMENT_QUERY = PY_LANGUAGE.query(
    """
    (block (expression_statement (string) @docstring))

    (comment) @comment
    """
)

# Remove comments and docstring
def remove_comments(code):
    parser = Parser(PY_LANGUAGE)
    source_bytes = bytes(code, "utf8")
    tree = parser.parse(source_bytes)
    capture_results = []
    for _, results in COMMENT_QUERY.captures(tree.root_node).items():
        capture_results += results

    capture_results.sort(key=lambda cap: cap.start_byte, reverse=True)

    for node in capture_results:
        source_bytes = source_bytes[: node.start_byte] + source_bytes[node.end_byte :]

    return source_bytes.decode("utf-8")
