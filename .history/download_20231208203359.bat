@echo off
:restart
set /p input=����ģ��:
set project=study
if "%input%"=="all" (
    echo ����ȫ��ģ��
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
    echo �������:ȫ��
) else if "%input%"=="children" (
    echo ������ģ��
    echo downloading %project%-project(children)
    echo --- start loading---:%project%-note
    cmd /c git clone https://gitee.com/LRoInt/%project%-note.git
    echo ---  end  loading---:%project%-note
    echo -
    echo --- start loading---:%project%-program
    cmd /c git clone https://gitee.com/LRoInt/%project%-program.git 
    echo ---  end  loading---:%project%-program
    echo �������:��ģ��
) else if "%input%"=="%project%-note" (
    echo downloading:%project%-note
    echo --- start loading---:%project%-note
    cmd /c git clone https://gitee.com/LRoInt/%project%-note.git
    echo ---  end  loading---:%project%-note
    echo �������:%project%-note
) else if "%input%"=="%project%-program" (
    echo downloading:%project%-program
    echo --- start loading---:%project%-program
    cmd /c git clone https://gitee.com/LRoInt/%project%-program.git 
    echo ---  end  loading---:%project%-program
    echo �������:%project%-program
)    
pause