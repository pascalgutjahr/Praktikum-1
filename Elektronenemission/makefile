all: build/emission.pdf /

build/emission.pdf: emission.tex | build
	lualatex --output-directory=build emission.tex
	biber --output-directory=build emission.bcf
	lualatex --output-directory=build emission.tex


build:
	mkdir -p build

clean:
	rm -rf build
