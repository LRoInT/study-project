import os


def walk_file(root, rfun, argv: str):
    for f_list in os.walk(root):
        f_dir = f_list[0]  # 源文件目录
        # f_name:源文件名
        for f_sub in f_list[1]:
            # 输入函数参数
            exec(f"rfun({argv})")
def del_history(file):
    if file[-8:]==".history":
        print(f"del {file}")
        os.system(f"del {file}")

walk_file(".",rfun=del_history,argv="os.path.join(f_dir,f_sub)")