FROM bitnami/minideb:latest

RUN apt update && apt dist-upgrade -y &&  apt install -y git build-essential cmake libusb-1.0-0-dev libopencv-dev libproj-dev


RUN git clone https://github.com/steve-m/librtlsdr.git /opt/librtlsdr 
RUN mkdir /opt/librtlsdr/build
WORKDIR /opt/librtlsdr/build
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DINSTALL_UDEV_RULES=ON ..
RUN make -j2 install

# load udev rules and blacklist the DVB driver shipped with the OS
RUN cp ../rtl-sdr.rules /etc/udev/rules.d/
RUN ldconfig
RUN mkdir -p /etc/modprobe.d
RUN echo 'blacklist dvb_usb_rtl28xxu' | tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf


RUN git clone https://github.com/pietern/goestools.git /opt/goestools
WORKDIR /opt/goestools
RUN git submodule init
RUN git submodule update --recursive
RUN mkdir /opt/goestools/build
WORKDIR /opt/goestools/build
RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..

# this will take a while on a raspberry pi
RUN make -j2 install 
WORKDIR /
