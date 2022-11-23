functional.py contains the following functions:

1) **sequential_map** - the function takes as arguments any number of functions and a container with some values. The function returns a list of the results of successively applying the passed functions to the values ​​in the container.

2) **consensus_filter** - the function accepts as arguments any number of functions that return True or False, as well as a container with some values. The function returns a list of values ​​that, when passed to all functions, evaluate to True.

3) **conditional_reduce** - the function accepts 2 functions, as well as a container with values. The first function takes 1 argument and returns True or False, the second also takes 2 arguments and returns a value. conditional_reduce returns a single value - the result of reduce, skipping the values ​​with which the first function returned False.

4) func_chain - the function accepts any number of functions as arguments and returns a function concatenating all passed by sequential execution.
Moreover **func_chain** has been integrated into **sequential_map**
