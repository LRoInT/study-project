# 项目管理工具
import download_lib
import sys
import json
from functools import partial

config = json.load(open("manager/config.json", "r", encoding="utf-8"))
download = partial(download_lib.download, config=config)


def main():
    while True:
        cmd = input(":")
        if cmd == "download":
            download(input("download:").split(","))
        elif cmd == "exit":
            sys.exit()


if __name__ == "__main__":
    while True:
        main()
