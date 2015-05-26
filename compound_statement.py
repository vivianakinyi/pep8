"""Compound statements (on the same line) are generally discouraged.
While sometimes it's okay to put an if/for/while with a small body
on the same line, never do this for multi-clause statements.
Also avoid folding such long lines!
Always use a def statement instead of an assignment statement that
binds a lambda expression directly to a name.
Okay: if foo == 'blah':\n do_blah_thing()
Okay: do_one()
Okay: do_two()
Okay: do_three()
E701: if foo == 'blah': do_blah_thing()
E701: for x in lst: total += x
E701: while t < 10: t = delay()
E701: if foo == 'blah': do_blah_thing()
E701: else: do_non_blah_thing()
E701: try: something()
E701: finally: cleanup()
E701: if foo == 'blah': one(); two(); three()
E702: do_one(); do_two(); do_three()
E703: do_four(); # useless semicolon
E704: def f(x): return 2*x
E731: f = lambda x: 2*x
"""