all: build/suszeptibil.pdf /

build/suszeptibil.pdf: suszeptibil.tex | build
	lualatex --output-directory=build suszeptibil.tex
	biber --output-directory=build suszeptibil.bcf
	lualatex --output-directory=build suszeptibil.tex


build:
	mkdir -p build

clean:
	rm -rf build
