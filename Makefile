all: build/stat.py

build/stat.py | build
python --output-directory=build stat.py

build:
	mkdir -p build

clean:
	rm -rf build
