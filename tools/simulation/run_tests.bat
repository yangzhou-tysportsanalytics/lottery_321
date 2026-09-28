@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Run the whole test suite on this PC and write a log.
rem  Double-click. Takes a few minutes; nothing is changed on disk except
rem  the log file test_logs\test_run_<date>.txt.
rem  Use it after changing any script.
rem ======================================================================
cd /d "%~dp0\..\.."
title NBA Lottery - test suite
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
set PYTHONPATH=%CD%\src\lottery321;%CD%\src\lottery321\ledgers
for /f "tokens=1-3 delims=/-. " %%a in ("%DATE%") do set STAMP=%%a%%b%%c
set LOG=test_logs\test_run_%STAMP%.txt
if not exist test_logs mkdir test_logs
echo Writing %LOG%
echo NBA Lottery 3-2-1 test suite, %DATE% %TIME% > "%LOG%"
%PY% -m unittest discover -s tests\lottery321 -p "test_*.py" -v >> "%LOG%" 2>&1
set RC=%ERRORLEVEL%
echo. >> "%LOG%"
%PY% -m unittest discover -s src\lottery321\ledgers -p "test_*.py" >> "%LOG%" 2>&1
if errorlevel 1 set RC=1
echo.
findstr /C:"Ran " /C:"OK" /C:"FAILED" "%LOG%"
echo.
if "%RC%"=="0" (
  echo All tests passed. The log is %LOG%.
) else (
  echo Some tests failed. See %LOG%.
)
pause
exit /b %RC%

:findpy
set "PY="
where py >nul 2>nul && (py -3 -c "import sys" >nul 2>nul && set "PY=py -3")
if not defined PY (
  python -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul && set "PY=python"
)
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PY="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not defined PY (
  echo Python 3 not found. Run run_primary.bat once first, it installs Python.
  pause
  exit /b 1
)
echo Using Python: %PY%
exit /b 0
