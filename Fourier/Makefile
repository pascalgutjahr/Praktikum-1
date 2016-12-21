all: build/fourier.pdf /

build/fourier.pdf: fourier.tex | build
	lualatex --output-directory=build fourier.tex
	biber --output-directory=build fourier.bcf
	lualatex --output-directory=build fourier.tex


build:
	mkdir -p build

clean:
	rm -rf build
