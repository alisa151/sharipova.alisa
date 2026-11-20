import operator
_UNESCAPE_PAIRS = (
    ("&lt;", "<"),
    ("&gt;", ">"),
    ("&quot;", '"'),
    ("'", "'"),
    ("&apos;", "'"),
    ("&amp;", "&"),
)
_ESCAPE_PAIRS = (
    ("&", "&amp;"),
    ("<", "&lt;"),
    (">", "&gt;"),
    ('"', "&quot;"),
    ("'", "'"),
)
def _replace_pair(text: str, pair: tuple[str, str]) -> str:
    old, new = pair
    return operator.methodcaller("replace", old, new)(text)
def _apply_replacements(text: str, pairs: tuple[tuple[str, str], ...]) -> str:
    result = text
    for pair in pairs:
        result = _replace_pair(result, pair)
    return result
def unescape_html(s: str) -> str:
    return _apply_replacements(s, _UNESCAPE_PAIRS)
def escape_html(s: str) -> str:
    return _apply_replacements(s, _ESCAPE_PAIRS)