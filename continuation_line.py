"""Continuation lines indentation.
Continuation lines should align wrapped elements either vertically
using Python's implicit line joining inside parentheses, brackets
and braces, or using a hanging indent.
When using a hanging indent these considerations should be applied:
- there should be no arguments on the first line, and
- further indentation should be used to clearly distinguish itself as a
continuation line.
Okay: a = (\n)
E123: a = (\n )
Okay: a = (\n 42)
E121: a = (\n 42)
E122: a = (\n42)
E123: a = (\n 42\n )
E124: a = (24,\n 42\n)
E125: if (\n b):\n pass
E126: a = (\n 42)
E127: a = (24,\n 42)
E128: a = (24,\n 42)
E129: if (a or\n b):\n pass
E131: a = (\n 42\n 24)
"""