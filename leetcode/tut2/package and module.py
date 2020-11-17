
不同文件夹import 需要用folername.pythonfilename.variablename
上面语法太长可以用alias，import foldername.pythonfilename as f


模块内置变量 __all__ = ["a", "c"]


package：就是个带 __init__.py 的文件夹
一个包(文件夹)下面应该有__init__.py文件，如果没有，那就是一个普通文件夹
调用时__init__.py文件下面的语句自动运行
在__init__.py里写__all__ = ["c7"]，只是导入c7模块(module)


# 换行 \ 或者 ()


import sys
print(sys.path)


import 时避免循环引入

import 导入模块的话，会执行模块里所有代码

