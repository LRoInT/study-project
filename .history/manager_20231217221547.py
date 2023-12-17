# 项目管理工具
from manager import *
import sys
import os
import json
from functools import partial

config = json.load(open("config.json", "r", encoding="utf-8"))
root = os.path.dirname(os.path.abspath(__file__))  # 项目根目录
cwd = root  # 工作目录
down_way = "git@"  # 仓库下载方式，默认为 ssh
download = partial(download.download, config=config, way=down_way) #固定 download函数 参数


def git():
    push = open(os.path.join(root, "git-push.bat"),
                "r", encoding="utf-8").read()
    os.system(push)
    for d in config['project_list']:
        os.chdir(os.path.join(root, config['project_list'][d]))
        print(os.getcwd())
        os.system(push)
    os.chdir(root)
    os.system("tree")


def main(cmd):  # 命令处理
    if cmd[0] == "download":  # 下载
        download(cmd[1:])
    elif cmd[0] == "git-push":  # 代码推送
        git()
    elif cmd[0] == "exit":  # 退出
        sys.exit()
    else:
        pass


argv = sys.argv.copy()
for e in range(len(argv)):
    if "exec:" in argv[e]:
        print(argv[e])
        exec(argv[e][5:])
if len(argv) == 1:
    while True:
        input_cmd = input(">>>").split(" ")
        main(input_cmd)
else:
    main(sys.argv[1:])
