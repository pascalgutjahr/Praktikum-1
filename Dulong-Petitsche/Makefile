all: build/dulong.pdf /

build/dulong.pdf: dulong.tex | build
	lualatex --output-directory=build dulong.tex
	biber --output-directory=build dulong.bcf
	lualatex --output-directory=build dulong.tex


build:
	mkdir -p build

clean:
	rm -rf build
