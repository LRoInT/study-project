@echo off
:restart
set /p input=������һ���ַ���:
if "%input%"=="all" (
    echo ����ȫ��ģ��
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
    echo �������:ȫ��
) else if "%input%"=="learn-note" (
    echo --- start loading---:learn-note
    cmd /c git clone https://gitee.com/LRoInt/learn-note.git
    echo ---  end  loading---:learn-note
    echo �������:learn-note
) else if "%input%"=="learn-note-program" (
    echo --- start loading---:learn-note-program
    cmd /c git clone https://gitee.com/LRoInt/learn-note-program.git 
    echo ---  end  loading---:learn-note-program
    echo �������:learn-note-program
)    
pause