build:
	docker build -t nickkb/goestools .

fresh: pull build

clean:
	rm -rf librtlsdr
	rm -rf goestools

pull: clean
	git clone https://github.com/steve-m/librtlsdr.git
	cd librtlsdr; \
	mkdir build
	git clone https://github.com/pietern/goestools.git
	cd goestools; \
	git submodule init; \
	git submodule update --recursive; \
	mkdir build


