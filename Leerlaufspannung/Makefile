all: build/leer.pdf /

build/leer.pdf: leer.tex | build
	lualatex --output-directory=build leer.tex
	biber --output-directory=build leer.bcf
	lualatex --output-directory=build leer.tex


build:
	mkdir -p build

clean:
	rm -rf build
