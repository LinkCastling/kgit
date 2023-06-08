import hashlib
import os

GIT_DIR = '.kgit'
OBJ_DIR = 'objects'


def init():
    # 我们用类似git的方式在文件夹下创建一个.kgit文件夹用于存储数据
    # 在Linux下该目录将会是隐藏的，Windows下将不会创建隐藏
    os.makedirs(GIT_DIR)
    # 创建一个存储对象的文件夹在.kgit文件夹下
    os.makedirs(os.path.join(GIT_DIR, OBJ_DIR))


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()  # oid为我们的哈希对象的名称（唯一表示）
    # 使用with代码块会自动关闭文件io
    # 使用wb（二进制写入模式）打开文件
    with open(os.path.join(GIT_DIR, OBJ_DIR, oid), 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    # rb形式读文件并返回
    with open(os.path.join(GIT_DIR, OBJ_DIR, oid), 'rb') as f:
        return f.read()
