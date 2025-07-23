# inkctx

inkctx 是面向 inkscape 的一个插件（扩展），用于载入 ConTeXt 排版结果到 inkscape 的当前图层。例如，用 ConTeXt 的数学公式或其他元素标注一些矢量图形，也可以用 MetaPost（或 MetaFun）绘制图形并插入到 inkscape 图层。

## 依赖

inkctx 包目前只能在 Linux 环境里使用，由以下文件组成：

* ctx.inx：插件窗口定义文件。
* ctx.py：插件功能实现。
* svg-from-pdf.sh：一份 bash 脚本，可将 pdf 文件转换问 svg 文件，并保证 svg 节点 id 不会出现冲突。
* safe-svg.awk：为 svg 节点 id 增加防冲突前缀的 awk 脚本。

故而 除了 inkscape（版本 >= 1.2）之外，inkctx 依赖 bash 和 gawk。

## 安装

运行 inkctx 源码目录中的 install.sh 脚本：

```console
$ sh install.sh
```

该脚本可将插件相关的文件复制到 ~/.config/inkscape/extensions 目录，若该目录与你的 Linux 里的 inkscape 插件目录不相符，可修改 install.sh 中的 `INKEX_PATH` 的值或手动复制相关文件到你的 inkscape 插件目录。

## 用法

打开 inkscape，通过菜单 Extensions / ConTeXt 可打开 inkctx 插件界面，在正文区域填写 ConTeXt 排版片段。模板区域可以定制 ConTeXt 排版样式，只是要注意，要保证模板内容中「`%{ConTeXt 片段}`」的存在。

更详细的用法说明见 [https://zhuanlan.zhihu.com/p/1931465282087518582](https://zhuanlan.zhihu.com/p/1931465282087518582)
