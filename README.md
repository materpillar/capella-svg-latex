# Capella + Jinja + SVG = Beautiful Latex

## Requirements:
- Python 3
- Texlive (Xetex)
- Inkscape

Prepare Python Environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run Tex and SVG files through Ninja
```bash
./main.py
```

Compile Tex report
```bash
xelatex --shell-escape tex/report.tex
```
