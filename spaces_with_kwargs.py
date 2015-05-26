"""Don't use spaces around the '=' sign in function arguments.
Don't use spaces around the '=' sign when used to indicate a
keyword argument or a default parameter value.
Okay: def complex(real, imag=0.0):
Okay: return magic(r=real, i=imag)
Okay: boolean(a == b)
Okay: boolean(a != b)
Okay: boolean(a <= b)
Okay: boolean(a >= b)
Okay: def foo(arg: int = 42):
E251: def complex(real, imag = 0.0):
E251: return magic(r = real, i = imag)
"""