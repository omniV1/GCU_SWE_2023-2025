#!/bin/bash

echo "Generating ABCs PDF..."
echo

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "ERROR: pandoc is not installed or not in PATH"
    echo "Please install pandoc from: https://pandoc.org/installing.html"
    echo "On macOS: brew install pandoc"
    echo "On Ubuntu/Debian: sudo apt-get install pandoc"
    echo "On CentOS/RHEL: sudo yum install pandoc"
    exit 1
fi

# Check if xelatex is installed
if ! command -v xelatex &> /dev/null; then
    echo "WARNING: xelatex not found. Trying with pdflatex..."
    PDF_ENGINE="pdflatex"
else
    PDF_ENGINE="xelatex"
fi

# Generate PDF using pandoc with eisvogel template and improved code block handling
pandoc "ABCs.md" \
    --from markdown \
    --to pdf \
    --template="../Templates/eisvogel.latex" \
    --listings \
    --pdf-engine="$PDF_ENGINE" \
    --pdf-engine-opt="-shell-escape" \
    --variable listings-disable-line-numbers=false \
    --variable code-block-font-size='\footnotesize' \
    --variable linestretch=1.1 \
    --output="ABCs.pdf" \
    --verbose

if [ $? -eq 0 ]; then
    echo
    echo "SUCCESS: PDF generated as 'ABCs.pdf'"
    echo "Code blocks have been optimized for proper line wrapping and page fitting."
    echo
    
    # Try to open the PDF
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open "ABCs.pdf"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open "ABCs.pdf" 2>/dev/null || echo "PDF generated. Please open manually."
    fi
else
    echo
    echo "ERROR: PDF generation failed."
    echo "Make sure you have:"
    echo "1. LaTeX distribution installed (TeX Live, MacTeX, etc.)"
    echo "2. All required LaTeX packages"
    echo "3. Proper file permissions"
    echo "4. The eisvogel template is properly configured"
    echo
    exit 1
fi 