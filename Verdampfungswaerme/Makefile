all: build/V203.pdf /

build/V203.pdf: V203.tex | build
	lualatex --output-directory=build V203.tex
	biber --output-directory=build V203.bcf
	lualatex --output-directory=build V203.tex

build:
	mkdir -p build

clean:
	rm -rf build
