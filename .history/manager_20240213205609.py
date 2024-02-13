# 项目管理工具
from manager import *
import sys
import os
import json
import getopt
from functools import partial
from datetime import datetime

config = json.load(open("config.json", "r", encoding="utf-8"))
cmd_project=partial(cmd_project, config=config)
root = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
cwd = root  # 工作目录
down_way = "git@"  # 仓库下载方式，默认为 ssh
site = "github" #默认下载站点
commit=datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"commit"
branch="origin/master"


def print_help():
    print("""
    Usage: python manager.py [OPTIONS]
    Options:
        -d, --download  下载项目
          all: 全部
          all-: 全部下属仓库
          <name>: 仓库名称
        -r, --repository  仓库
          -c, --commit 提交信息
          -b, --branch 分支
        -h, --help  帮助
    """)


if sys.argv[1:]:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:hs:w:r:c:b:", [
                                   "download=", "way=", "site=", "repository=", "commit=", "branch="])
    except getopt.GetoptError:
        print("输入异常")
        sys.exit(2)
    for i in opts:
        if i[0] == "-w" or i[0] == "--way":
            down_way = i[1]
        elif i[0] == "-s" or i[0] == "--site":
            site = i[1]
        elif i[0] =="-c" or i[0] == "--commit":
            commit = i[1]
            if "%t"in commit:
                commit=commit.replace("%t",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif i[0] == "-b" or i[0] == "--branch":
            branch = i[1]
    for opt in opts:
        if opt[0] == "-d" or opt[0] == "--download":
            for d in cmd_project(opt[1]):
                clone_project(d, config, site, down_way)
        elif opt[0] == "-r" or opt[0] == "--repository":
            for d in cmd_project(opt[1]):
                git_cmd(d,commit,branch)
else:
    print_help()
    sys.exit()
