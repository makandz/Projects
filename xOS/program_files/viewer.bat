echo Enter the location of the file you wish to view.
echo.
set /p location=[USER - ADVANCE VIEWER]: 

cls

echo Advance Text Viewer - Made by MastaCoder (Alpha)
echo ---------------------------------------------------------

if exist %location% (
	for /f "tokens=*" %%a in (%location%) do (
		echo %%a
	)
	echo ---------------------------------------------------------
	goto :funcs

) else (
	echo File not found!
	echo ---------------------------------------------------------
	echo Press any key to return to xOS..
	pause>nul
	goto :clear
)

:funcs
	set /p command=exit - del: 

	if "%command%" == "exit" (
		goto :clear
	)
	if "%command%" == "del" (
		del>nul %location%
		echo File has been deleted successfully, press any key to exit..
		pause>nul
		goto :clear
	)