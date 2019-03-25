all: build/roentgen.pdf /

build/roentgen.pdf: roentgen.tex | build
	lualatex --output-directory=build roentgen.tex
	biber --output-directory=build roentgen.bcf
	lualatex --output-directory=build roentgen.tex


build:
	mkdir -p build

clean:
	rm -rf build
