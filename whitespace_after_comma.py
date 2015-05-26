"""Each comma, semicolon or colon should be followed by whitespace.
Okay: [a, b]
Okay: (3,)
Okay: a[1:4]
Okay: a[:4]
Okay: a[1:]
Okay: a[1:4:2]
E231: ['a','b']
E231: foo(bar,baz)
E231: [{'a':'b'}]
"""

[a,b]
['a', 'b']
a[1: 4: 2]
