"""Comparison to singletons should use "is" or "is not".
Comparisons to singletons like None should always be done
with "is" or "is not", never the equality operators.
Okay: if arg is not None:
E711: if arg != None:
E711: if None == arg:
E712: if arg == True:
E712: if False == arg:
Also, beware of writing if x when you really mean if x is not None --
e.g. when testing whether a variable or argument that defaults to None was
set to some other value. The other value might have a type (such as a
container) that could be false in a boolean context!
"""

if arg is not None:

if arg != None:

if None == arg:

if arg == True:

if False == arg:
	