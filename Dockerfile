#
# Copyright 2023 isobar. All Rights Reserved.
#
# The isobar python image
#
# Usage:
#       dk build -t isobar/app:1.0.0 -f Dockerfile .
#
FROM isobar/pytorch:1.0.0
LABEL maintainer "jacky.huang@isobar.com"

WORKDIR /app

COPY . .
