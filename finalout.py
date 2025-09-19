import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from io import BytesIO

def add_covers(input_pdf_path, cover_img_path, backcover_img_path, output_pdf_path):
    # 创建封面PDF（使用实际A4尺寸）
    cover_buffer = BytesIO()
    c = canvas.Canvas(cover_buffer, pagesize=A4)
    # 直接使用图片原始尺寸（假设图片已经是A4大小）
    img = ImageReader(cover_img_path)
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1], preserveAspectRatio=False)
    c.showPage()
    c.save()
    
    # 创建空白页
    blank_buffer = BytesIO()
    c = canvas.Canvas(blank_buffer, pagesize=A4)
    img = ImageReader(os.path.join(current_dir, "op.jpg"))
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1], preserveAspectRatio=False)
    c.showPage()
    c.save()
    
    # 创建封底PDF（使用实际A4尺寸）
    backcover_buffer = BytesIO()
    c = canvas.Canvas(backcover_buffer, pagesize=A4)
    img = ImageReader(backcover_img_path)
    c.drawImage(img, 0, 0, width=A4[0], height=A4[1], preserveAspectRatio=False)
    c.showPage()
    c.save()
    
    # 合并PDF
    merger = PdfWriter()
    
    # 添加封面
    cover_buffer.seek(0)
    merger.append(cover_buffer)
    
    # 添加空白页
    blank_buffer.seek(0)
    merger.append(blank_buffer)
    
    # 添加原始内容
    merger.append(input_pdf_path)
    
    # 添加封底
    backcover_buffer.seek(0)
    merger.append(backcover_buffer)
    
    # 保存结果
    with open(output_pdf_path, "wb") as f:
        merger.write(f)

if __name__ == "__main__":
    # 获取当前文件夹路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 文件路径
    input_pdf = os.path.join(current_dir, "main.pdf")
    cover_img = os.path.join(current_dir, "cover.jpg")
    backcover_img = os.path.join(current_dir, "backcover.jpg")
    output_pdf = os.path.join(current_dir, "output.pdf")
    
    # 执行添加封面封底
    add_covers(input_pdf, cover_img, backcover_img, output_pdf)
    print(f"处理完成！已生成: {output_pdf}")