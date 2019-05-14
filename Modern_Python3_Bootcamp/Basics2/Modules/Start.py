import Modules

# When module file is imported, module executable code will run

Modules.testing()
Modules.calculate(45, 45)

# Object for module class must be first created for accessing class functions
obj = Modules.Demo()
obj.testing2()