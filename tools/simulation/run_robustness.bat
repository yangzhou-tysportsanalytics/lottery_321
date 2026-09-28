@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Simulation robustness runs (addendum A1 section 5). Four short runs, one
rem  after another:
rem    dta       draw-then-adjust lottery procedure   (81 game days)
rem    latelink  win model fitted on earlier late windows (81 days)
rem    stress    win-model slope x1.25                (81 days)
rem    alt6      2024 WAS 13-30 alternative ledger reading (25 days)
rem  Start it after the primary and norestr runs. Resumable.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - robustness
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
for %%V in (dta latelink stress alt6) do (
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
echo All robustness runs finished. You can close this window.
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
