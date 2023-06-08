import argparse
import os
import sys

from . import data
from .data import GIT_DIR


def main():
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()  # 创建一个参数解析器

    commands = parser.add_subparsers(dest='command')  # 创建了一个子命令解析器
    commands.required = True  # 表明这个子命令一定是必需的，用户必需提供一个有效的子命令

    init_parser = commands.add_parser('init')  # 定义了一个init子命令解析器
    init_parser.set_defaults(func=init)  # 设置了init子命令调用的默认函数

    #  我们引入了一个hash objects用于存储对象
    #  我们使用哈希来引用对象
    #  这种类型的存储称为内容可寻址存储
    hash_object_parser = commands.add_parser("hash-object")  # 创建一个hash对象的子命令解析器
    hash_object_parser.set_defaults(func=hash_object)  # 去调用hash_object方法
    hash_object_parser.add_argument('file')  # 为hash-object增加一个参数

    # 一个新的命令：cat-file
    # 这个命令与hash-object相反，通过这个命令我们可以通过OID读取对象
    # 本质是打开.kgit/objects/{OID}
    cat_file_parser = commands.add_parser("cat-file")
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')
    return parser.parse_args()  # 返回参数解析结果


def init(args):
    data.init()  # 创建.kgit子目录
    print('Initialized empty kgit repository in %s' % os.path.join(os.getcwd(), GIT_DIR))


def hash_object(args):
    # 将传入的文件，打开并交给data模块处理
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))


def cat_file(args):
    sys.stdout.flush()  # 属性标准输出流
    sys.stdout.buffer.write(data.get_object(args.object))  # 调用data模块的方法返回对象信息
