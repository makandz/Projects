goto :top_bar_draw

:main_system
	set /p result=[USER]: 
	(echo COMMAND %result%)>>system_access/system_log.xOS
	for /f "tokens=1" %%G IN ("%result%") DO findstr /i /r /c:"^[ ]*:%%G\>" "%~f0" >nul 2>nul && goto %%G
	if errorlevel 1 goto :command_not_found

:help
	echo.
	echo # These are your available commands:
	echo ---------------------------------------------------------
	echo # SHOW [arg]	: Shows text written after it.
	echo # REMOVE [arg]	: Remove a file.
	echo # CLEAR 	: Clear the system written log.
	echo # READ 		: Prints current saved memory.
	echo # WRITE 	: Overwrite to saved memory.
	echo # PRINT [arg]	: Print text of a file. (UTF Format)
	echo # RESET 	: Resets the current saved logs.
	echo ---------------------------------------------------------
	echo.
	goto :main_system

:show
	echo.
	set result=%result:show =%
	echo # %result%
	echo.
	goto :main_system

:remove
	set result=%result:remove =%
	echo.
	if exist %result% (
		del>nul %result%
		echo # Delete successful.
	) else (
		echo # Selected file does not exist!
	)
	echo.
	goto :main_system

:reset
	cd system_access
	if exist memory.xOS (del memory.xOS)
	if exist temp.xOS (del temp.xOS)
	if exist system_log.xOS (del system_log.xOS)
	(echo.)>memory.xOS
	(echo.)>temp.xOS
	(echo.)>system_log.xOS
	echo.
	echo # Restarting..
	cd..
	start /max main.bat
	exit

:clear
	cls
	goto :top_bar_draw

:print
	set result=%result:print =%
	echo.
	if exist %result% (
		for /f "tokens=*" %%a in (%result%) do (
			echo %%a
		)
	) else (
		echo # %result% NOT FOUND.
	)
	echo.
	goto :main_system

:create
	echo.
	set result=%result:create =%
	if exist %result% (del %result%)
	:b
		set /p write=[USER - WRITE]: 
		if "%write%" == "exit" (
			echo.
			GOTO :main_system
		)
		(echo %write%)>>%result%
		goto :b

:write
	echo.
	cd system_access
	if exist memory.xOS (del memory.xOS)
	:a
		set /p write=[USER - WRITE]: 
		IF "%write%" == "exit" (
			echo.
			cd..
			GOTO :main_system
		)
		(echo %write%)>>memory.xOS
		goto :a

:read
	echo.
	cd system_access
	if exist memory.xOS (
		for /f "tokens=*" %%a in (memory.xOS) do (
			echo %%a
		)
	) else (
		echo # memory.xOS NOT FOUND.
	)
	cd..
	echo.
	goto :main_system

:list
	echo.
	set result=%result:list =%
	if "%result%" == "list" (goto :c)
	set /p ="# " <nul
	dir %result% >nul
	if errorlevel 1 (
		echo.
		goto :main_system
	)
	echo Following files and folders found!
	echo.
	dir /b %result%
	echo.
	goto :main_system
	:c
		echo # Following files and folders found!
		echo.
		dir /b
		echo.
		goto :main_system

:run
	set result=%result:run =%
	echo.
	if exist program_files/%result%.bat (
		cls
		call program_files/%result%.bat
		goto :clear
	) else (
		echo # Program not found.
		echo.
		goto :main_system
	)
	


:command_not_found
	(echo ERROR %result%)>>system_access/system_log.xOS
	echo.
	echo # The following command was not found!
	echo.
	goto :main_system

:top_bar_draw
	echo xOS Developer Preview Alpha - v0.01
	echo ------------------------------------------------
	goto :main_system

:restart
	start /max main.bat
	exit

:exit
	del system_access/temp.xOS
	exit

pause