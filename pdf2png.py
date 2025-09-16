import fitz  # PyMuPDF
from PIL import Image
import os

# 直接在代码中指定文件路径和参数
input_pdf_path = "chapbub.pdf"  # 请替换为你的PDF文件路径
output_png_path = "chapbub.png"  # 请替换为你想要的输出PNG文件路径
target_size = (2480, 3508)  # 目标尺寸：宽 x 高
render_dpi = 300  # 渲染DPI，越高越清晰，但处理时间更长且占用更多内存

try:
    # 检查输入文件是否存在
    if not os.path.isfile(input_pdf_path):
        raise FileNotFoundError(f"输入的PDF文件未找到: {input_pdf_path}")

    # 打开PDF文档
    doc = fitz.open(input_pdf_path)
    
    # 检查是否为单页PDF
    if len(doc) != 1:
        doc.close()
        raise ValueError("本脚本仅支持单页PDF文件转换。")
    
    # 加载第一页
    page = doc.load_page(0)
    
    # 计算缩放矩阵以高质量渲染
    zoom_factor = render_dpi / 72  # PDF的默认DPI为72
    matrix = fitz.Matrix(zoom_factor, zoom_factor)
    
    # 将PDF页面渲染为像素图(pixmap)
    pix = page.get_pixmap(matrix=matrix)
    
    # 将pixmap转换为PIL Image对象
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # 使用高质量的重采样滤波器调整图像至目标尺寸
    img_resized = img.resize(target_size, Image.LANCZOS)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)
    
    # 保存为PNG文件
    img_resized.save(output_png_path, "PNG")
    print(f"转换成功！文件已保存至: {output_png_path}")
    
    # 关闭PDF文档
    doc.close()
    
except Exception as e:
    print(f"转换过程中发生错误: {str(e)}")