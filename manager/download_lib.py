# 管理工具下载模块
from os import system
import os
import json
from sys import exit



def download(*argv,config):
    for i in argv:
        i=i[0]
        if i == "all":
            system(f"git clone {config['project']}")
            os.chdir(f"./{config['project'].split('/')[-1]}")
            for n in config["project_list"]:
                system(f"git clone {config['project_list'][n]}")
        elif i == "project":
            system(f"git clone {config['project']}")
        elif i == "children":
            for n in config["project_list"]:
                system(f"git clone {config['project_list'][n]}")
        else:
            try:
                system(f"git clone {config['project_list'][i]}")
            except:
                print("不存在该项目")
