@echo off
IF "%~1" NEQ "" (
   Set "process=%~1.exe"
   echo "killing process %process%"
   taskkill /IM /F /T %process%
)
