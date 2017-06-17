all: build/optik.pdf /

build/optik.pdf: optik.tex | build
	lualatex --output-directory=build optik.tex
	biber --output-directory=build optik.bcf
	lualatex --output-directory=build optik.tex


build:
	mkdir -p build

clean:
	rm -rf build
