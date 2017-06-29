all: build/millikan.pdf /

build/millikan.pdf: millikan.tex | build
<<<<<<< HEAD
	lualatex --output-directory=build millikan.tex
	biber --output-directory=build millikan.bcf
	lualatex --output-directory=build millikan.tex
||||||| merged common ancestors
	lualatex --output-directory=build millikan.tex
  biber --output-directory=build millikan.bcf
  lualatex --output-directory=build millikan.tex
=======
		lualatex --output-directory=build millikan.tex
  	biber --output-directory=build millikan.bcf
  	lualatex --output-directory=build millikan.tex
>>>>>>> kacke


build:
	mkdir -p build

clean:
	rm -rf build
