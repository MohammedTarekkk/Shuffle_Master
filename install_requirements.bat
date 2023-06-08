@echo off

REM Set the path to the Python executable
SET PYTHON_EXECUTABLE=C:/Python39/python.exe

REM Set the path to the requirements file
SET REQUIREMENTS_FILE=requirements.txt

REM Change the current directory to the directory of the batch file
CD /D "%~dp0"

REM Install the required libraries using pip
%PYTHON_EXECUTABLE% -m pip install -r %REQUIREMENTS_FILE%

REM Check the exit code of the previous command
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while installing the required libraries.
    pause
    exit /b
)
