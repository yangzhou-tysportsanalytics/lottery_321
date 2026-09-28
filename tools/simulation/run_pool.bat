@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Pooled-rights convergence check (exploratory).
rem  Re-runs 12 pre-selected primary game days with 32 sampled joint draft
rem  orders per world instead of 4; same seeds, same states, same number of
rem  worlds as the primary run. Everything else is unchanged.
rem  About 1 hour per day per process; with all cores but one, roughly
rem  3 hours in all. Resumable: finished days are skipped, so it is safe to
rem  close the window and double-click again later.
rem  Do NOT run this at the same time as another simulation window.
rem  When it prints ALL DONE it also writes the comparison tables
rem  (results\exploratory_4\R23_*.csv).
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - pooled-rights convergence check
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
echo.
echo === Run pool32 ===
%PY% run_simulation.py --variant pool32 %*
if errorlevel 1 (
  echo Run pool32 failed. Please check the messages above.
  pause
  exit /b 1
)
echo.
echo === Comparison with the primary run ===
%PY% ..\..\src\lottery321\pool_convergence.py analyse --draws 32
if errorlevel 1 (
  echo The comparison failed. Please check the messages above.
  pause
  exit /b 1
)
echo.
echo Pooled-rights check finished. You can close this window.
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
