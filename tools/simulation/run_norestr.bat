@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Simulation sensitivity run WITHOUT the repeat restrictions (tag norestr).
rem  Start it after the primary run has finished. Same 312 game days.
rem  Safe to close and restart: finished game days are kept and skipped.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - norestr
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
echo.
echo === Full run (norestr). Leave this window open. ===
%PY% run_simulation.py --variant norestr %*
echo.
echo Finished. You can close this window.
pause
exit /b 0

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
