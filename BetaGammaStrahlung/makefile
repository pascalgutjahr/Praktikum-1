all: build/strahlung.pdf /

build/strahlung.pdf: strahlung.tex | build
	lualatex --output-directory=build strahlung.tex
	# biber --output-directory=build strahlung.bcf
	# lualatex --output-directory=build strahlung.tex


build:
	mkdir -p build

clean:
	rm -rf build
