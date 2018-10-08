echo           ___    ____         _              _   _                
echo  __  __  / _ \  / ___^|       / \     _ __   ^| ^| (_)  _ __     ___ 
echo  \ \/ / ^| ^| ^| ^| \___ \      / _ \   ^| '_ \  ^| ^| ^| ^| ^| '_ \   / _ \
echo   ^>  ^<  ^| ^|_^| ^|  ___) ^|    / ___ \  ^| ^|_) ^| ^| ^| ^| ^| ^| ^| ^| ^| ^|  __/
echo  /_/\_\  \___/  ^|____/    /_/   \_\ ^| .__/  ^|_^| ^|_^| ^|_^| ^|_^|  \___^|
echo                                     ^|_^|                           
echo.

set /p ="Creating temp.xOS file.. " <nul
(
echo # xOS TEMP FILE
echo # This file is used to store information on each process.
)>system_access/temp.xOS
echo Ok.

set /p ="Setting console colors.. " <nul
color 0F
echo Ok.

set /p ="Verifying system file: memory.xOS.. " <nul
if exist system_access/memory.xOS (
	echo Ok.
) else (
	echo Not Found.
)

set /p ="Checking for startup.xOS file.." <nul
if exist system_access/startup.xOS (
	echo Ok. & echo.
	for /f "tokens=*" %%a in (system_access/startup.xOS) do (
		%%a
	)
) else (
	echo Not Found.
)

echo.
echo # Loading complete! Taking you to the main screen.

timeout 3 >nul
cls

if exist system_files/system.bat (
	call system_files/system.bat
) else (
	echo missing system file..
	pause>nul
)