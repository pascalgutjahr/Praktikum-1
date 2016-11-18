all: build/lockin.pdf /

build/lockin.pdf: lockin.tex | build
	lualatex --output-directory=build lockin.tex
	biber --output-directory=build lockin.bcf
	lualatex --output-directory=build lockin.tex

build:
	mkdir -p build

clean:
	rm -rf build
