TARGET=cv
all: $(TARGET)

cv: .
ifdef public
	python proc.py --public teaching.tex money.tex
else
	python proc.py teaching.tex money.tex
endif
	latexrun cv
	echo
	echo
	echo "use public=1 to strip private content"
	echo "Did you run genpubs.py in ~/code/homepage ?"


