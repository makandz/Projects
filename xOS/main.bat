@ECHO OFF

echo ## MastaCoder .xOS BIOS ##
echo --------------------------------------------------

echo Checking for input devices..
echo.

if exist input/autorun.bat (
	call input/autorun.bat
	goto :complete
)

echo Press any key to skip..
timeout>nul 5

if exist system_files/startup.bat (
	cls
	call system_files/startup.bat
) else (
	echo Missing required startup file..
	goto :complete
)

:complete
	pause>nul