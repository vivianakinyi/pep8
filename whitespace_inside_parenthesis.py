"""Avoid extraneous whitespace.
Avoid extraneous whitespace in these situations:
- Immediately inside parentheses, brackets or braces.
- Immediately before a comma, semicolon, or colon.
Okay: spam(ham[1], {eggs: 2})
E201: spam( ham[1], {eggs: 2})
E201: spam(ham[ 1], {eggs: 2})
E201: spam(ham[1], { eggs: 2})
E202: spam(ham[1], {eggs: 2} )
E202: spam(ham[1 ], {eggs: 2})
E202: spam(ham[1], {eggs: 2 })
E203: if x == 4: print x, y; x, y = y , x
E203: if x == 4: print x, y ; x, y = y, x
E203: if x == 4 : print x, y; x, y = y, x
"""
spam(ham[1], {eggs: 2})
spam(ham[1], {eggs: 2} )
