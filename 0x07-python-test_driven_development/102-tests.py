import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不
lib.print_python_string(s)
s = "숟가락은 존재하
lib.print_python_string(s)
s = "スプーンは"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
