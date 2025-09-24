@echo off
echo Generating ABCs PDF...
echo.

REM Check if pandoc is installed
pandoc --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pandoc is not installed or not in PATH
    echo Please install pandoc from: https://pandoc.org/installing.html
    echo Download the Windows installer and make sure pandoc is in your PATH
    pause
    exit /b 1
)

REM Check if xelatex is installed
xelatex --version >nul 2>&1
if %errorlevel% neq 0 (
    echo WARNING: xelatex not found. Trying with pdflatex...
    set PDF_ENGINE=pdflatex
) else (
    set PDF_ENGINE=xelatex
)

REM Generate PDF using pandoc with eisvogel template and improved code block handling
pandoc "Assignments/Topic1/ABCs.md" ^
    --from markdown ^
    --to pdf ^
    --template="Templates/eisvogel.latex" ^
    --listings ^
    --pdf-engine=%PDF_ENGINE% ^
    --pdf-engine-opt="-shell-escape" ^
    --variable listings-disable-line-numbers=false ^
    --variable code-block-font-size='\footnotesize' ^
    --variable linestretch=1.1 ^
    --output="Assignments/Topic1/ABCs.pdf" ^
    --verbose

if %errorlevel% equ 0 (
    echo.
    echo SUCCESS: PDF generated as 'Assignments/Topic1/ABCs.pdf'
    echo Code blocks have been optimized for proper line wrapping and page fitting.
    echo.
    
    REM Try to open the PDF
    start "" "Assignments/Topic1/ABCs.pdf"
) else (
    echo.
    echo ERROR: PDF generation failed.
    echo Make sure you have:
    echo 1. LaTeX distribution installed ^(MiKTeX, TeX Live, etc.^)
    echo 2. All required LaTeX packages
    echo 3. Proper file permissions
    echo 4. The eisvogel template is properly configured
    echo.
    pause
    exit /b 1
)

pause 