@echo off

REM Set the path to the Python executable
SET PYTHON_EXECUTABLE=C:/Python39/python.exe

REM Change the current directory to the directory of the batch file
CD /D "%~dp0"

REM Run the Python script
%PYTHON_EXECUTABLE% "sys_meeting_tool.py"
