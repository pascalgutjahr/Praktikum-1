all: build/statisch.py

build/statisch.py | build
python --output-directory=build statisch.py

build:
	mkdir -p build

clean:
	rm -rf build
