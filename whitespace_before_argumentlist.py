"""Avoid extraneous whitespace.
Avoid extraneous whitespace in the following situations:
- before the open parenthesis that starts the argument list of a
function call.
- before the open parenthesis that starts an indexing or slicing.
Okay: spam(1)
E211: spam (1)
Okay: dict['key'] = list[index]
E211: dict ['key'] = list[index]
E211: dict['key'] = list [index]
"""
spam(1)
spam (1)