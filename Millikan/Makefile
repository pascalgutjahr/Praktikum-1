all: build/millikan.pdf /

build/millikan.pdf: millikan.tex | build
	lualatex --output-directory=build millikan.tex
  biber --output-directory=build millikan.bcf
  lualatex --output-directory=build millikan.tex



build:
	mkdir -p build

clean:
	rm -rf build
