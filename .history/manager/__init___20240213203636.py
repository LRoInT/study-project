import os


def clone_link(func):
    def wrapper(*args, **kwargs):
        print(args)
    return wrapper


@clone_link
def system(x):
    os.system(x)


def cmd_project(cmd, config):
    if cmd == "all":
        return list(config["project"].values())  # 全部仓库
    elif cmd == "all-":
        return list(config["project"].values())[1:]  # 除根仓库外
    elif cmd in config["project"]:
        return [config["project"][cmd]]


def clone_project(project, config, site, down_way):
    # down_way + site + project
    if down_way == "git@":
        link = down_way+config["load"][site][0]+":"+config["load"][site][1]
    else:
        link = down_way+config["load"][site][0]+"/"+config["load"][site][1]
    print("Cloning " + project)
    system("git clone " + link + project)
    print(f"{project} cloned")


git_cmd_list = [
    "git init",
    "git add .",
    "git commit -m '{}'",
    "git pull {}"
    "git push {}",
]


def git_cmd(path,commit, branch):
    branch = branch.replace("/", " ")
    def cmd():
        git_cmd_list[2] = git_cmd_list[2].format(commit)
        git_cmd_list[3] = git_cmd_list[3].format(branch)
        git_cmd_list[4] = git_cmd_list[4].format(path)
        return git_cmd_list
    for c in cmd():
        system(c)
