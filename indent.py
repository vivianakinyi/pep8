"""Never mix tabs and spaces.
The most popular way of indenting Python is with spaces only. The
second-most popular way is with tabs only. Code indented with a mixture
of tabs and spaces should be converted to using spaces exclusively. When
invoking the Python command line interpreter with the -t option, it issues
warnings about code that illegally mixes tabs and spaces. When using -tt
these warnings become errors. These options are highly recommended!
Okay: if a == 0:\n a = 1\n b = 1
E101: if a == 0:\n a = 1\n\tb = 1
"""
if a == 0:
    a = 1 
    b = 1

