import click

def strip(public, inf, outf):
  for l in inf:
    if l.strip().startswith("##"):
      if public:  continue
      l = l[2:]

    outf.write(l)


@click.command()
@click.option("--public", is_flag=True, default=False, help="Set flag to hide lines prefixed with ##")
@click.argument("fnames", nargs=-1)
def main(public, fnames):
  for fname in fnames:
    name = fname.split(".")[0]
    outname = "%s_stripped.tex" % name
    with open(fname, "r") as inf:
      with open(outname, "w") as outf:
        strip(public, inf, outf)

if __name__ == "__main__":
  main()
