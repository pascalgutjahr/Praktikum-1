all: build/dreh.pdf /

build/dreh.pdf: dreh.tex | build
	lualatex --output-directory=build dreh.tex
	biber --output-directory=build dreh.bcf
	lualatex --output-directory=build dreh.tex


build:
	mkdir -p build

clean:
	rm -rf build
