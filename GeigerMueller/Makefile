all: build/geiger.pdf /

build/geiger.pdf: geiger.tex | build
	lualatex --output-directory=build geiger.tex
	# biber --output-directory=build geiger.bcf
	# lualatex --output-directory=build geiger.tex


build:
	mkdir -p build

clean:
	rm -rf build
