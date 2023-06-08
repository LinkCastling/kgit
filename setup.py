from setuptools import setup

# 配置我们的包，使得用户可以通过kgit命令调用kgit.cli模块中的main函数
setup(name='kgit',
      version='1.0',
      packages=['kgit'],
      entry_points={
          'console_scripts': [
              'kgit= kgit.cli:main'
          ]
      })
"""
在Windows环境下执行kgit命令提示'kgit' 不是内部或外部命令，也不是可运行的程序或批处理文件。注解检测Python环境变量配置
"""
