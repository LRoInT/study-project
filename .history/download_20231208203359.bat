@echo off
:restart
set /p input=下载模块:
set project=study
if "%input%"=="all" (
    echo 下载全部模块
    echo downloading %project%-project
    echo --- start loading---:%project%-project
    cmd /c git clone https://gitee.com/LRoInt/%project%-project
    echo ---  end  loading---:%project%-project
    echo -
    cd %project%-project
    echo .>cd>%project%-project
    echo -
    echo --- start loading---:%project%-note
    cmd /c git clone https://gitee.com/LRoInt/%project%-note.git
    echo ---  end  loading---:%%project%-note
    echo -
    echo --- start loading---:%project%-program
    cmd /c git clone https://gitee.com/LRoInt/%project%-program.git 
    echo ---  end  loading---:%project%-program
    echo 下载完成:全部
) else if "%input%"=="children" (
    echo 下载子模块
    echo downloading %project%-project(children)
    echo --- start loading---:%project%-note
    cmd /c git clone https://gitee.com/LRoInt/%project%-note.git
    echo ---  end  loading---:%project%-note
    echo -
    echo --- start loading---:%project%-program
    cmd /c git clone https://gitee.com/LRoInt/%project%-program.git 
    echo ---  end  loading---:%project%-program
    echo 下载完成:子模块
) else if "%input%"=="%project%-note" (
    echo downloading:%project%-note
    echo --- start loading---:%project%-note
    cmd /c git clone https://gitee.com/LRoInt/%project%-note.git
    echo ---  end  loading---:%project%-note
    echo 下载完成:%project%-note
) else if "%input%"=="%project%-program" (
    echo downloading:%project%-program
    echo --- start loading---:%project%-program
    cmd /c git clone https://gitee.com/LRoInt/%project%-program.git 
    echo ---  end  loading---:%project%-program
    echo 下载完成:%project%-program
)    
pause