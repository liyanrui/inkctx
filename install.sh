#!/bin/bash

INKEX_PATH=~/.config/inkscape/extensions

if [ ! -e "$INKEX_PATH" ]; then
    mkdir -p "$INKEX_PATH"
fi
cp ctx.* svg-from-pdf.sh safe-svg.awk "$INKEX_PATH"
