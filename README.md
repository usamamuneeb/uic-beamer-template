## Beamer template for UIC

This is a LaTeX Beamer template crafted for University of Illinois Chicago according to the university's [style guide](https://marketing.uic.edu/marketing-toolbox/university-style-guide/).

This template has been derived from the Overleaf template for [SINTEF](https://www.overleaf.com/latex/templates/sintef-presentation/jhbhdffczpnx). Multiple iterations have been done on the example slides to demonstrate the most useful Beamer features. Some extra commands have been added to solve minor issues.

### Quick start

You can [use this template directly on Overleaf](https://www.overleaf.com/latex/templates/uic-presentation-template/dgjbtyvtgqcg).

### Support for OpenType fonts

This template supports OpenType fonts if used with XeLaTeX (set as default on Overleaf template). You should never call the compiler directly. Always call it via `latexmk`.

```bash
latexmk -pdf -pdflatex='xelatex' main.tex
```

> **Note**: We typically use the above command, because by default, using `latexmk` via the `-xetex` option invokes `xelatex` with the `-no-pdf` flag. This causes it to generate an intermediate DVI file, which is later converted to PDF using the `xdvipdfmx` tool. 

pdfLaTeX can still be used, except that instead of the included fonts, it will use font packages from your TeX distribution (exhaustive list provided in the [LaTeX Font Catalog](https://tug.org/FontCatalogue)).

```bash
latexmk -pdf main.tex
```
