import os


def clone_link(func):
    def wrapper(*args, **kwargs):
        print(args)
    return wrapper


def system(x):
    os.system(x)


def clone_project(project, config, site, down_way):
    # down_way + site + project
    if down_way == "git@":
        link = down_way+config["load"][site][0]+":"+config["load"][site][1]
    else:
        link = down_way+config["load"][site][0]+"/"+config["load"][site][1]
    if project == "all":
        for p in list(config["project_list"].values()):
            print("Cloning "+link + p)
            system("git clone " + link + p)
        print("All projects cloned")
    if project == "all-":
        for p in list(config["project_list"].values())[1:]:
            print("Cloning " + p)
            system("git clone " + link + p)
        print("All projects cloned")
    elif project in config["project_list"]:
        print("Cloning " + config["project_list"][project])
        system("git clone " + link + config["project_list"][project])
        print(f"{project} cloned")
