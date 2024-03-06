# CV template

This repo contains scaffold to generate [eugene wu's](https://eugenewu.net) CV.


Setup

    pip install click

Run

    # generates cv.pdf
    make


    # strips out all lines prefixed with '##' in money.tex and teaching.tex
    make public=1


I wrote a short python script to auto-generate the contents of `pubs.tex` so it has the same
formatting as the rest of the CV.

