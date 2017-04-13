all: build/ultra.pdf /

build/ultra.pdf: ultra.tex | build
	lualatex --output-directory=build ultra.tex
	biber --output-directory=build ultra.bcf
	lualatex --output-directory=build ultra.tex


build:
	mkdir -p build

clean:
	rm -rf build
