all: build/beugung.pdf /

build/beugung.pdf: beugung.tex | build
	lualatex --output-directory=build beugung.tex
	biber --output-directory=build beugung.bcf
	lualatex --output-directory=build beugung.tex


build:
	mkdir -p build

clean:
	rm -rf build
