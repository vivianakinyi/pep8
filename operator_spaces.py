"""Surround operators with a single space on either side.
- Always surround these binary operators with a single space on
either side: assignment (=), augmented assignment (+=, -= etc.),
comparisons (==, <, >, !=, <=, >=, in, not in, is, is not),
Booleans (and, or, not).
- If operators with different priorities are used, consider adding
whitespace around the operators with the lowest priorities.
Okay: i = i + 1
Okay: submitted += 1
Okay: x = x * 2 - 1
Okay: hypot2 = x * x + y * y
Okay: c = (a + b) * (a - b)
Okay: foo(bar, key='word', *args, **kwargs)
Okay: alpha[:-i]
E225: i=i+1
E225: submitted +=1
E225: x = x /2 - 1
E225: z = x **y
E226: c = (a+b) * (a-b)
E226: hypot2 = x*x + y*y
E227: c = a|b
E228: msg = fmt%(errno, errmsg)
"""