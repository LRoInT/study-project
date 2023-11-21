@echo off
:restart
set /p input=请输入一个字符串:
if "%input%"=="all" (
    echo 下载全部模块
    echo learn-note-project
    echo --- start loading---:learn-note-project
    cmd /c git clone https://gitee.com/LRoInt/learn-note-project
    echo ---  end  loading---:learn-note-project
    echo -
    cd learn-note-project
    echo .>cd>learn-note-project
    echo -
    echo --- start loading---:learn-note
    cmd /c git clone https://gitee.com/LRoInt/learn-note.git
    echo ---  end  loading---:learn-note
    echo -
    echo --- start loading---:learn-note-program
    cmd /c git clone https://gitee.com/LRoInt/learn-note-program.git 
    echo ---  end  loading---:learn-note-program
    echo 下载完成:全部
) else if "%input%"=="learn-note" (
    echo --- start loading---:learn-note
    cmd /c git clone https://gitee.com/LRoInt/learn-note.git
    echo ---  end  loading---:learn-note
    echo 下载完成:learn-note
) else if "%input%"=="learn-note-program" (
    echo --- start loading---:learn-note-program
    cmd /c git clone https://gitee.com/LRoInt/learn-note-program.git 
    echo ---  end  loading---:learn-note-program
    echo 下载完成:learn-note-program
)    
pause