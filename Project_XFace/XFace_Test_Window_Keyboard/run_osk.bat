@echo off
echo Set objShell = CreateObject("Shell.Application") > "%temp%\run_osk.vbs"
echo objShell.ShellExecute "osk.exe", "", "", "runas", 0 >> "%temp%\run_osk.vbs"
"%temp%\run_osk.vbs"
