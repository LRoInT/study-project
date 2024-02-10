# 项目管理工具
from manager import *
import sys
import os
import json
from functools import partial
import getopt

config = json.load(open("config.json", "r", encoding="utf-8"))
root = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
cwd = root  # 工作目录
down_way = "git@"  # 仓库下载方式，默认为 ssh
site = "github"


def print_help():
    print("""
    Usage: python manager.py [OPTIONS]
    Options:
        -d, --download=<download>  下载项目
          all: 全部
          all-: 全部下属仓库
          <name>: 仓库名称
        -h, --help                 帮助
    """)


if sys.argv[1:]:
    opts, args = getopt.getopt(sys.argv[1:], "d:h:", ["download="])
    for opt in range(len(opts)):
        if opts[opt][0] == "-d" or opts[opt][0] == "--download":
            down_list = opts[opt][1].split(",")
            for i in down_list:
                if i[0] == "-w" or i[0] == "--way":
                    down_way = i[1]
                elif i[0] == "-s" or i[0] == "--site":
                    site = i[1]
            for d in down_list:
                clone_project(d, config, site, down_way)
else:
    print_help()
    sys.exit()
