FROM alpine AS base

RUN apk add --no-cache opencv-dev zlib && rm -rf /var/cache/apk/*


FROM base AS build

RUN apk add --no-cache cmake build-base && rm -rf /var/cache/apk/*

COPY ./goestools /goestools
WORKDIR /goestools/build

RUN cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && make -j2 install 

FROM base 

COPY --from=build /usr/share/goestools /usr/share/goestools
COPY --from=build /usr/bin/goes* /usr/bin/
