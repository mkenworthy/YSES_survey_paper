import numpy as np
import paths
from astropy.io import ascii
from astropy.table import Table

t = Table.read(paths.data / "YSES_paper - targets.csv")

print(t)
ascii.write(t, paths.data / "table_targets.tex", Writer=ascii.Latex, latexdict=ascii.latex.latexdicts['AA'])

ldict = ascii.latex.latexdicts['AA']
ldict['tabletype'] = 'longtable'
print(ldict)
ascii.write(t, paths.data / "table_targets_long.tex",
    Writer=ascii.Latex,
    latexdict=ascii.latex.latexdicts['AA'])
ascii.write(t, paths.data / "table_targets_long.tex",
    Writer=ascii.Latex,
    latexdict=ldict)
