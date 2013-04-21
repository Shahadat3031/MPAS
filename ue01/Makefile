CC=pandoc
CFLAGS=--latex-engine=xelatex -V mainfont="Source Sans Pro" \
	      -V geometry="left=2cm,right=2cm,bottom=1.5cm" \
		  --smart -V lang="ngerman" -V monofont="Source Code Pro" -V sansfont="Source Sans Pro" \
		  -V fontsize="10pt" \
		  --standalone
FILENAME=ue01

all: $(FILENAME).pdf

%.md: %_knit_.md %.r
	Rscript -e "library(knitr); knit('$<','$@')"

%.pdf: %.md
	$(CC) -o $@ $(CFLAGS) $<

clean:
	find . -name "*.md" -and \
		-not -name "*_knit_.md" -or \
		-name "*.pdf" | xargs rm
