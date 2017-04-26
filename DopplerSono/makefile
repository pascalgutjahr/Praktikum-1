all: build/sono.pdf /

build/sono.pdf: sono.tex | build
	lualatex --output-directory=build sono.tex
	biber --output-directory=build sono.bcf
	lualatex --output-directory=build sono.tex


build:
	mkdir -p build

clean:
rm -rf build
