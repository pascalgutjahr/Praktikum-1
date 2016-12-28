all: build/pendel.pdf /

build/pendel.pdf: pendel.tex | build
	lualatex --output-directory=build pendel.tex
	biber --output-directory=build pendel.bcf
	lualatex --output-directory=build pendel.tex


build:
	mkdir -p build

clean:
	rm -rf build
