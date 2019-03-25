all: build/frank.pdf /

build/frank.pdf: frank.tex | build
	lualatex --output-directory=build frank.tex
	biber --output-directory=build frank.bcf
	lualatex --output-directory=build frank.tex


build:
	mkdir -p build

clean:
	rm -rf build
