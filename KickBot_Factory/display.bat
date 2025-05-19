@echo off
setlocal enabledelayedexpansion
for /F "delims=" %%f in ('git ls-tree -r --name-only HEAD') do (
    set "file=%%f"
    set "file=!file:/=\!"
    echo ==== %%f ====
    type "!file!"
    echo.
)
