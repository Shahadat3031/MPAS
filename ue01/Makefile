CC=pandoc
CFLAGS=--latex-engine=xelatex -V mainfont="Source Sans Pro" \
	      -V geometry="left=2cm,right=2cm,bottom=1.5cm" \
		  --smart -V lang="ngerman" -V monofont="Source Code Pro" -V sansfont="Source Sans Pro" \
		  --listings --standalone
FILENAME=ue01

all: $(FILENAME).pdf

%.pdf: %.code.md
	$(CC) -o $@ $(CFLAGS) $<

%.code.md: %.md

