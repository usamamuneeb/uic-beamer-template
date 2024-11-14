## Beamer template for UIC

This is a LaTeX Beamer template crafted for University of Illinois Chicago according to the university's [style guide](https://marketing.uic.edu/marketing-toolbox/university-style-guide/).

This template has been derived from the Overleaf template for [SINTEF](https://www.overleaf.com/latex/templates/sintef-presentation/jhbhdffczpnx). Multiple iterations have been done on the example slides to demonstrate the most useful Beamer features. Some extra commands have been added to solve minor issues.

### Quick start

You can [use this template directly on Overleaf](https://www.overleaf.com/latex/templates/uic-presentation-template/dgjbtyvtgqcg).

### Support for OpenType fonts

This template supports OpenType fonts if used with XeLaTeX (set as default on Overleaf template). If you have references, your compile command should look like this:

```bash
xelatex main && bibtex main && xelatex main && xelatex main
```

**Note**: Even if you don't have any references, you still need to run the compiler at least twice, to get the PDF page numbers right.

pdfLaTeX can still be used, except that instead of the included fonts, it will use font packages from your TeX distribution (exhaustive list provided in the [LaTeX Font Catalogue](https://tug.org/FontCatalog)). To build, you can do something similar to above (replacing `xelatex` with `pdflatex` or you can use `latexmk`)

```bash
latexmk -pdf main.tex
```
