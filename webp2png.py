import os
from PIL import Image

def convert_webp_to_png():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.webp'):
            # 构建完整的文件路径
            webp_path = os.path.join(current_dir, filename)
            
            # 生成PNG文件名（替换扩展名）
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(current_dir, png_filename)
            
            try:
                # 打开WEBP文件并转换为PNG
                with Image.open(webp_path) as img:
                    # 如果图像有透明度通道，保留RGBA模式
                    if img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGBA')
                    else:
                        img = img.convert('RGB')
                    
                    # 保存为PNG格式
                    img.save(png_path, 'PNG')
                    print(f"转换成功: {filename} -> {png_filename}")
            
            except Exception as e:
                print(f"转换失败 {filename}: {str(e)}")

if __name__ == "__main__":
    convert_webp_to_png()