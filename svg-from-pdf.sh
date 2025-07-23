#!/bin/bash
SELF_PATH="$(dirname $0)"

## 记录 svg 编号
# 该文件中的内容是一个每次增 1 的数字
# 在下面的 awk 脚本里，会将该数字作为 svg 文档中元素 id 名字前缀的一部分
SVG_N=/tmp/alloc-id-for-inkex
if [ ! -e $SVG_N ]; then
   echo "1" > $SVG_N
fi

# 将 pdf 转换为 svg
# 可以用 pdf2svg "$1" "$2".tmp
# 既然是为 inkscape 写扩展，也可以用 inkscape 将 pdf 转换为 svg
# $1 是 pdf 文件路径，$2 是 svg 文件路径
inkscape "$1" --pdf-poppler --export-type=svg --export-filename "$2" \
         && mv "$2" "$2".tmp

# 为 svg 文件中各个元素的 id 以及 id 引用增加具备唯一性的前缀，以避免
# 在 inkscape 导入该文件时，元素 id 与之前导入的 svg 元素出现冲突。
awk -v svg_num_file=$SVG_N \
    -f "$SELF_PATH"/safe-svg.awk "$2".tmp > "$2"
