# 管理工具下载模块
from os import system
import os
import json
from sys import exit


def download(*argv, config, way):
    for i in argv:
        i = i[0]
        d = ""
        if "gitee:" in i:
            site="gitee"

        if "github:" in i:
            site="gitbub"
        
        d = i.split(site)[1][1:]
        if way=="git@":
            l=f"{way}{config['load'][site][0]}:{config['load'][site][1]}"
        
        print(i)
        print(d)
        print(l)

        if d == "all":
            system(f"git clone {l+config['project']}")
            os.chdir(f"./{config['project'].split('/')[-1]}")
            for n in config["project_list"]:
                system(f"git clone {l+config['project_list'][n]}")
        elif d == "project":
            system(f"git clone {l+config['project']}")
        elif d == "children":
            for n in config["project_list"]:
                system(f"git clone {l+config['project_list'][n]}")
        else:
            try:
                system(f"git clone {l+config['project_list'][i]}")
            except:
                print("不存在该项目")
