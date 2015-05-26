"""Separate top-level function and class definitions with two blank lines.
Method definitions inside a class are separated by a single blank line.
Extra blank lines may be used (sparingly) to separate groups of related
functions. Blank lines may be omitted between a bunch of related
one-liners (e.g. a set of dummy implementations).
Use blank lines in functions, sparingly, to indicate logical sections.
Okay: def a():\n pass\n\n\ndef b():\n pass
Okay: def a():\n pass\n\n\n# Foo\n# Bar\n\ndef b():\n pass
E301: class Foo:\n b = 0\n def bar():\n pass
E302: def a():\n pass\n\ndef b(n):\n pass
E303: def a():\n pass\n\n\n\ndef b(n):\n pass
E303: def a():\n\n\n\n pass
E304: @decorator\n\ndef a():\n pass
"""


def a():
    pass


def b():
    pass
