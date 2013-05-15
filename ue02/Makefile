CC=pandoc
DATADIR=../data
IMG_DIR=$(DATADIR)/img
TEMPLATE=fucd

CFLAGS=-S -s --self-contained -f markdown -t dzslides --slide-level=2 \
	   --data-dir=$(DATADIR) --template=$(TEMPLATE) --mathjax
FILES=$(shell ls *_knitr_.md)

.PHONY: all pdf web clean deploy img

all: $(FILES:_knitr_.md=.html)

%.md: %_knit_.md %.r
	Rscript -e "library(knitr); knit('$<','$@')"

%.html: %.md
	$(CC) $(CFLAGS) -o $@

clean:
	find . -name "*.md" -and \
		-not -name "*_knit_.md" -or \
		-name "*.pdf" | xargs rm
