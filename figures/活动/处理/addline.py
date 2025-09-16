from PIL import Image
import os

# 定义颜色和高度参数
TOP_BLANK_HEIGHT = 60  # pt (总空白高度)
COLOR1 = "#D6B1D3"    # 顶部和底部边框颜色
COLOR2 = "#690065"    # 主紫色区域颜色

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 支持的图片格式
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

for filename in os.listdir(current_dir):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        try:
            # 打开图片
            img_path = os.path.join(current_dir, filename)
            img = Image.open(img_path)
            
            # 计算新尺寸（pt转像素，1pt=1.333px）
            pt_to_px = 4 / 3
            total_blank_px = int(TOP_BLANK_HEIGHT * pt_to_px)
            
            # 创建新图片（RGB模式）
            new_width = img.width
            new_height = img.height + total_blank_px
            new_img = Image.new('RGB', (new_width, new_height), (255, 255, 255))
            
            # 创建顶部彩色区域
            top_bar = Image.new('RGB', (img.width, total_blank_px), (255, 255, 255))
            
            # 填充颜色区域
            # 1. 顶端1像素: #D6B1D3
            top_bar.paste(Image.new('RGB', (img.width, 1), COLOR1), (0, 0))
            
            # 2. 下面11像素: #690065
            top_bar.paste(Image.new('RGB', (img.width, 11), COLOR2), (0, 1))
            
            # 3. 再下面1像素: #D6B1D3
            top_bar.paste(Image.new('RGB', (img.width, 1), COLOR1), (0, 12))
            
            # 组合图片
            new_img.paste(top_bar, (0, 0))
            new_img.paste(img, (0, total_blank_px))
            
            # 保存图片（覆盖原文件）
            new_img.save(img_path)
            print(f"已处理: {filename}")
            
        except Exception as e:
            print(f"处理 {filename} 时出错: {str(e)}")

print("所有图片处理完成！")