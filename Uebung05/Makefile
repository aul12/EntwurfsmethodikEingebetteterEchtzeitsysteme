RUBBER=rubber
SCREEN=screen
VIEWER=xdg-open
DOT=dot

all: main.pdf

show: main.pdf
	$(SCREEN) -dm $(VIEWER) main.pdf

main.pdf: main.tex control.pdf *.m
	$(RUBBER) -d main.tex

%.eps: %.svg
	inkscape $< -E $@ --export-ignore-filters --export-ps-level=3

%.pdf: %.dot
	$(DOT) -T pdf -o $@ $<

clean: clean-temp
	rm -f *.pdf
	rm -f *.zip
	rm -f *.npy

clean-temp:
	$(RUBBER) --clean main.tex
	rm -f *.eps
	rm -f *-eps-converted-to.pdf
	rm -f *.log
