import os

def walk_file(root, rfun=os.system):
    for f_list in os.walk(root):
        f_dir = f_list[0]  # 源文件目录
        # f_name:源文件名
        if ".history" in f_dir:
            for f in f_list[2]:
                os.system(f"del {os.path.join(f_dir, f)}")
            for f in f_list[1]:
                walk_file(os.path.join(f_dir, f))
            os.rmdir(f_dir)
walk_file(".")

