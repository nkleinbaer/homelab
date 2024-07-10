build:
	docker build -t goestools .

fresh: pull build

clean:
	rm -rf goestools

pull: clean
	git clone https://github.com/pietern/goestools.git
	cd goestools; \
	git submodule init; \
	git submodule update --recursive; \
	mkdir build


