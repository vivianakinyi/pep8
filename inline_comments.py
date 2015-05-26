"""Separate inline comments by at least two spaces.
An inline comment is a comment on the same line as a statement. Inline
comments should be separated by at least two spaces from the statement.
They should start with a # and a single space.
Each line of a block comment starts with a # and a single space
(unless it is indented text inside the comment).
Okay: x = x + 1 # Increment x
Okay: x = x + 1 # Increment x
Okay: # Block comment
E261: x = x + 1 # Increment x
E262: x = x + 1 #Increment x
E262: x = x + 1 # Increment x
E265: #Block comment
E266: ### Block comment
"""
### Block comment
x = x + 1  # Increment x