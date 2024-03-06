# CV template

This repo contains scaffold to generate [eugene wu's](https://eugenewu.net) [CV](http://eugenewu.net/files/statement/cv.pdf).


Setup

    pip install click

Edit [pubs.yml](./pubs.yml) with your papers.  Then generate [pubs.tex](pubs.tex)

    python genpubs.py -a pubs.yml > pubs.tex


Generate CV

    # include all content
    make

    # strip out all lines prefixed with '##' in money.tex and teaching.tex
    make public=1



