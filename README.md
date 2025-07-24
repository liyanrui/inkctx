# inkctx

inkctx 是面向 inkscape（版本 >= 1.2）的一个插件（扩展），用于载入 ConTeXt 排版结果到 inkscape 的当前图层。例如，用 ConTeXt 的数学公式或其他元素标注一些矢量图形，也可以用 MetaPost（或 MetaFun）绘制图形并插入到 inkscape 图层。

## 安装

inkctx 包由以下文件组成：

* ctx.inx：插件窗口定义文件。
* ctx.py：插件功能实现。

运行 inkctx 源码目录中的 install.sh 脚本：

```console
$ sh install.sh
```

该脚本可将 ctx.inx 和 ctx.py 复制到 ~/.config/inkscape/extensions 目录，若该目录与你的 Linux 里的 inkscape 插件目录不相符，可修改 install.sh 中的 `INKEX_PATH` 的值或手动j将这两份文件到你的 inkscape 插件目录。

inkctx 需要你的系统已经安装了 ConTeXt 包，若未安装它，可参考

* [ConTeXt wiki 上的安装指南](https://wiki.contextgarden.net/Introduction/Installation)
* [ConTeXt 蹊径](http://github.com/liyanrui/ConTeXt-notes)

## 用法

打开 inkscape，通过菜单 Extensions / ConTeXt 可打开 inkctx 插件界面，在正文区域填写 ConTeXt 排版片段。模板区域可以定制 ConTeXt 排版样式，只是要注意，要保证模板内容中「`%{ConTeXt 片段}`」的存在。

更详细的用法说明见 [https://zhuanlan.zhihu.com/p/1931465282087518582](https://zhuanlan.zhihu.com/p/1931465282087518582)
