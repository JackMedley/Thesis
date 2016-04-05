# ~/bin/bash
#"pdflatex" -interaction=nonstopmode ZJetsPaper.tex
#"bibtex" ZJetsPaper
#"pdflatex" -interaction=nonstopmode ZJetsPaper.tex
#"pdflatex" -interaction=nonstopmode ZJetsPaper.tex
#rm *.dvi *.ps *.log *.aux *.toc *.blg *.fdb_latexmk *.fls 2>/dev/null || true

"pdflatex"  thesis.tex
"bibtex"    thesis
"pdflatex"  thesis.tex
"pdflatex"  thesis.tex
rm *.dvi *.ps *.log *.aux *.toc *.blg *.bbl *.lof *.out *.lot *.fdb_latexmk *.fls 2>/dev/null || true

