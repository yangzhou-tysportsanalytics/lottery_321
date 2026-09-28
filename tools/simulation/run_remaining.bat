@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Everything left after norestr, in one go. Double-click ONCE, after the
rem  norestr window has printed ALL DONE. Runs, in order:
rem    dta       draw-then-adjust lottery procedure        (81 game days)
rem    latelink  win model fitted on earlier late windows  (81 days)
rem    stress    win-model slope x1.25                     (81 days)
rem    alt6      2024 WAS 13-30 alternative ledger reading (25 days)
rem    c3        component decomposition, 24 configs       (81 days)
rem  About 19 hours in total. Resumable: finished days are skipped, so it is
rem  safe to close the window and double-click again later.
rem  Do NOT run this at the same time as another simulation window: each run
rem  already uses every core but one, so two at once only slows both down.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - remaining runs
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
set "NORESTR=..\..\simulations\norestr"
set N=0
for /f %%C in ('dir /s /b "%NORESTR%\exposures_*.npz" 2^>nul ^| find /c /v ""') do set N=%%C
echo norestr: %N% of 312 game days done.
if %N% LSS 312 (
  echo.
  echo norestr has not finished yet. Let it finish first, then double-click this again.
  echo Running both at once still works, but the two runs share the same cores
  echo and both take longer.
  choice /c YN /n /m "Run anyway? [Y=yes, N=quit] "
  if errorlevel 2 exit /b 1
)
for %%V in (dta latelink stress alt6 c3) do (
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
echo All remaining simulation runs finished. You can close this window.
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
