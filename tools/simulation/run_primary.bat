@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Simulation runner (NBA Lottery 3-2-1). Double-click to start.
rem  1) finds Python 3 or installs it with winget (per user, no admin)
rem  2) installs numpy and tzdata
rem  3) runs a 1-minute smoke test, then the full primary run
rem  Safe to close and restart: finished game days are kept and skipped.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation

set "PY="
where py >nul 2>nul && (py -3 -c "import sys" >nul 2>nul && set "PY=py -3")
if not defined PY (
  python -c "import sys; assert sys.version_info >= (3, 10)" >nul 2>nul && set "PY=python"
)
if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PY="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
if not defined PY (
  echo Python 3 not found. Installing Python 3.12 with winget ...
  winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
  if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set PY="%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
  ) else (
    echo.
    echo Could not install Python automatically. Please install Python 3.12 from https://www.python.org/downloads/
    echo ^(tick "Add python.exe to PATH"^), then double-click this file again.
    pause
    exit /b 1
  )
)
echo Using Python: %PY%
%PY% --version

echo Installing numpy and tzdata ...
%PY% -m pip install --user --quiet --disable-pip-version-check numpy tzdata
if errorlevel 1 (
  echo pip install failed. Check the internet connection and try again.
  pause
  exit /b 1
)

set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1

echo.
echo === Smoke test (about 1 minute) ===
%PY% run_simulation.py --smoke --workers 2
if errorlevel 1 (
  echo Smoke test failed. Please check the messages above.
  pause
  exit /b 1
)

echo.
echo === Full run (primary). Leave this window open; the PC will not go to sleep while it runs. ===
%PY% run_simulation.py %*
echo.
echo Finished. You can close this window.
pause
