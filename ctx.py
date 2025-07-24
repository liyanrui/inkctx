#!/usr/bin/env python3
import inkex
import os
import subprocess
import tempfile
from inkex.utils import debug

class ConTeXt(inkex.GenerateExtension):
    def add_arguments(self, pars):
        pars.add_argument("--cmd", type=str, default="")
        pars.add_argument("--template", type=str, default="")
        pars.add_argument("--ctx", type=str, default="")
        pars.add_argument("--context-gui", type=str, default="")
        
    def get_selection_center(self):
        if not self.svg.selection:
            return (0, 0)  # 无选区时默认画布左上角
        bbox = self.svg.selection.bounding_box()
        return (bbox.center_x, bbox.center_y)
    
    def process_defs(self, defs_element):
        all_ids = self.svg.get_ids()  # 获取文档所有现有 ID
        for def_element in defs_element:
            # 生成不冲突的随机 ID
            def_element.set_random_ids(backlinks=True, blacklist=all_ids)
            # 添加到文档 defs 区域
            self.svg.defs.append(def_element)
            # 更新 ID 黑名单（避免后续元素冲突）
            all_ids.add(def_element.get_id())
            
    def generate(self):
        with tempfile.NamedTemporaryFile(suffix=".tex", mode="w+t", delete=True) as src:
            # 获得临时目录的路径
            tmp_path = tempfile.gettempdir()
            # 构造 ConTeXt 源文档
            ctx_text = self.options.template.replace("\\n", "\n")
            ctx_text = ctx_text.replace("%{ConTeXt 片段}", self.options.ctx.replace("\\n", "\n"))
            src.write(ctx_text)
            src.flush()
            # 调用 context 命令
            subprocess.run([self.options.cmd, "--purgeall", src.name], cwd = tmp_path,
                            check = True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # 构造 pdf 文件名，即去掉 src.name 的 .tex 后缀，换成 .pdf
            file_name_no_ext = os.path.splitext(src.name)[0]
            pdf_path = os.path.join(tmp_path, file_name_no_ext + ".pdf")
            svg_path = os.path.join(tmp_path, file_name_no_ext + ".svg")
            subprocess.run(['inkscape', pdf_path, '--pdf-poppler',
                            '--export-type=svg', '--export-filename', svg_path],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # 载入 svg，创建组，取无 .svg 后缀的文件名作为组名
            svg_obj = inkex.elements.load_svg(svg_path)
            g = inkex.Group.new(file_name_no_ext)
            for child in svg_obj.getroot():
                if isinstance(child, inkex.ShapeElement):
                    g.append(child)
                elif isinstance(child, inkex.Defs):
                    # 处理定义元素（化解 id 重复）
                    self.process_defs(child)
            # 定位
            unit = self.svg.unittouu("1pt")
            viewbox = svg_obj.getroot().get_viewbox()
            tx, ty = self.get_selection_center()
            #### svg 摆放是以其左上角顶点定位的，现将定位点移动到 svg 图形中心
            if tx > 0:
                tx -= (0.5 * viewbox[2]) * unit
            if ty > 0:
                ty -= (0.5 * viewbox[3]) * unit
            #### 先平移变换，将 svg 中心与选区中心对准，然后再缩放。
            g.transform = inkex.Transform(f"translate({tx}, {ty})") @ inkex.Transform(scale=unit)
            
            # 删除 pdf 和 svg 文件
            os.remove(pdf_path)
            os.remove(svg_path)
            
            # 返回包含了 svg 的组
            return g

if __name__ == "__main__":
    #debug(os.environ['PATH'])
    #debug(os.getcwd())
    ConTeXt().run()
