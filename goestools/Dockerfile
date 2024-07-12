FROM alpine  AS build

RUN apk add --no-cache opencv-dev zlib cmake build-base && rm -rf /var/cache/apk/*

COPY ./goestools /goestools
WORKDIR /goestools/build

RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && make -j2 install 

FROM alpine 

COPY --from=build /usr/lib/libXau.so.6 /usr/lib/libXdmcp.so.6 /usr/lib/libunistring.so.5 /usr/lib/libunistring.so.5 \
		  /usr/lib/libbrotlicommon.so.1 /usr/lib/libglapi.so.0 /usr/lib/libdrm.so.2 /usr/lib/libX11.so.6 /usr/lib/libxcb-glx.so.0 \
		  /usr/lib/libxcb.so.1 /usr/lib/libX11-xcb.so.1 /usr/lib/libxcb-dri2.so.0 /usr/lib/libXext.so.6 /usr/lib/libXfixes.so.3 \
		  /usr/lib/libXxf86vm.so.1 /usr/lib/libxcb-shm.so.0 /usr/lib/libexpat.so.1 /usr/lib/libxshmfence.so.1 /usr/lib/libxcb-randr.so.0 \
		  /usr/lib/libxcb-dri3.so.0 /usr/lib/libxcb-present.so.0 /usr/lib/libxcb-sync.so.1 /usr/lib/libxcb-xfixes.so.0 /usr/lib/libgfortran.so.5 \
		  /usr/lib/libsharpyuv.so.0 /usr/lib/libzstd.so.1 /usr/lib/libImath-3_1.so.29 /usr/lib/libIlmThread-3_1.so.30 /usr/lib/libIex-3_1.so.30 \
		  /usr/lib/libcares.so.2 /usr/lib/libnghttp2.so.14 /usr/lib/libidn2.so.0 /usr/lib/libpsl.so.5 /usr/lib/libzstd.so.1 /usr/lib/libbrotlidec.so.1 \
		  /usr/lib/libbsd.so.0 /usr/lib/libmd.so.0 /usr/lib/libGL.so.1 /usr/lib/libopenblas.so.3 /usr/lib/libtbb.so.12 /usr/lib/libjpeg.so.8 \
		  /usr/lib/libwebp.so.7 /usr/lib/libpng16.so.16 /usr/lib/libtiff.so.6 /usr/lib/libopenjp2.so.7 /usr/lib/libOpenEXR-3_1.so.30 /usr/lib/libsqlite3.so.0 \
		  /usr/lib/libcurl.so.4 /usr/lib/libtiff.so.6 /usr/lib/libopencv* /usr/lib/libproj.so.25 /usr/lib/libstdc++.so.6 /usr/lib/libgcc_s.so.1 \
      /usr/lib 

COPY --from=build /usr/share/goestools /usr/share/goestools
COPY --from=build /usr/bin/goes* /usr/bin/

