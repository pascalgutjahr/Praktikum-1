all: build/waermepumpe.pdf /

build/waermepumpe.pdf: waermepumpe.tex | build
	lualatex --output-directory=build waermepumpe.tex
	biber --output-directory=build waermepumpe.bcf
	lualatex --output-directory=build waermepumpe.tex


build:
	mkdir -p build

clean:
	rm -rf build
