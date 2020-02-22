@echo off
IF "%~1" NEQ "" (
   echo "killing process %~1.exe"
   "%__APPDIR__%taskkill.exe" /F /IM "%~1.exe" /T
)
