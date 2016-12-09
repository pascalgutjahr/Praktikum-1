all: build/schwingung.pdf /

build/schwingung.pdf: schwingung.tex | build
	lualatex --output-directory=build schwingung.tex
	biber --output-directory=build schwingung.bcf
	lualatex --output-directory=build schwingung.tex


build:
	mkdir -p build

clean:
	rm -rf build
