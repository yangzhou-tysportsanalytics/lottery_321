@echo off
setlocal EnableExtensions
rem ======================================================================
rem  Corrected draw-then-adjust run (dta2).
rem  The 81 game days, states and seeds of the dta run, with the corrected
rem  repair of src\lottery321\dta_corrected.py. The dta folder is not touched.
rem  Resumable: finished days are skipped, so it is safe to close the window
rem  and double-click again later. Do NOT run this at the same time as
rem  another simulation window.
rem ======================================================================
cd /d "%~dp0"
title NBA Lottery simulation - dta2 (corrected draw-then-adjust)
call :findpy || exit /b 1
set OMP_NUM_THREADS=1
set OPENBLAS_NUM_THREADS=1
set MKL_NUM_THREADS=1
echo.
echo === Tests ===
pushd ..\..
%PY% -m unittest tests/lottery321/test_dta_corrected.py
if errorlevel 1 (
  popd
  echo Tests failed. Nothing was run. Please check the messages above.
  pause
  exit /b 1
)
popd
echo.
echo === Run dta2 ===
%PY% run_simulation.py --variant dta2 %*
if errorlevel 1 (
  echo Run dta2 failed. Please check the messages above.
  pause
  exit /b 1
)
echo.
echo === Analysis and comparison with the primary run ===
%PY% ..\..\src\lottery321\analysis.py dta2
%PY% ..\..\src\lottery321\analysis.py --compare primary dta2
%PY% ..\..\src\lottery321\robustness_headlines.py dta2 --out robustness_headlines_dta2.csv
echo.
echo dta2 finished. You can close this window.
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
