all: build/traegheitsmoment.pdf /

build/traegheitsmoment.pdf: traegheitsmoment.tex | build
	lualatex --output-directory=build traegheitsmoment.tex
	biber --output-directory=build traegheitsmoment.bcf
	lualatex --output-directory=build traegheitsmoment.tex

build:
	mkdir -p build

clean:
	rm -rf build
