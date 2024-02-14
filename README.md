## Beamer template for UIC

This is a LaTeX Beamer template crafted for University of Illinois Chicago according to the university's [style guide](https://marketing.uic.edu/marketing-toolbox/university-style-guide/).

### Quick start

You can [use this template directly on Overleaf](https://www.overleaf.com/latex/templates/uic-presentation-template/dgjbtyvtgqcg).

### Support for OpenType fonts

This template supports OpenType fonts if used with `XeLaTeX` (set as default on Overleaf template):

```bash
xelatex main.tex
```

`pdfLaTeX` can still be used, except that instead of the included fonts, it will use font packages listed in the [LaTeX Font Catalogue](https://tug.org/FontCatalogue).

```bash
pdflatex main.tex
```

### Credits

This template has been derived from the Overleaf template for [SINTEF](https://www.overleaf.com/latex/templates/sintef-presentation/jhbhdffczpnx). I have simplified the example slides and additionally, have also included a pseudocode example slide.
