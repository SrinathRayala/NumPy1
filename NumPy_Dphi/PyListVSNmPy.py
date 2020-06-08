import numpy as np
from timeit import Timer
size_of_vec = 1000
X_list = range(size_of_vec)
Y_list = range(size_of_vec)
X = np.arange(size_of_vec)
Y = np.arange(size_of_vec)

def pure_python_version():
    z=[X_list[i] + Y_list[i] for i in range(len(X_list))]
def numpy_version():
    Z= X+Y
timer_obj1 = Timer("pure_python_version()",
                   "from __main__ import pure_python_version")
timer_ojb2 = Timer("numpy_version()",
                   "from __main__ import numpy_version")
print("Pure python Verion",timer_obj1.timeit(10))
print("NumPy Version",timer_ojb2.timeit(10))
