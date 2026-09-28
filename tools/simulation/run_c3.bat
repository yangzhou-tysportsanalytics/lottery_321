@echo off
setlocal EnableExtensions
rem ======================================================================
rem  C3 component decomposition (C3 registration). 24 configurations
rem  on the 81-day subsample. This is the longest of the sensitivity runs
rem  (roughly three times the cost of a primary day per day of the subsample).
rem  Start it after the primary run. Resumable: finished days are skipped.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - C3
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
for %%V in (c3) do (
  echo.
  echo === Run %%V ===
  %PY% run_simulation.py --variant %%V %*
  if errorlevel 1 (
    echo Run %%V failed. Please check the messages above.
    pause
    exit /b 1
  )
)
echo.
echo C3 run finished. You can close this window.
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
