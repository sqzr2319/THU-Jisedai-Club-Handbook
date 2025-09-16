import os
from PIL import Image
import argparse

def convert_webp_to_png(folder_path):
    """
    递归地将文件夹中的所有WebP图像转换为PNG格式
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.webp'):
                webp_path = os.path.join(root, file)
                png_path = os.path.splitext(webp_path)[0] + '.png'
                
                try:
                    # 打开WebP图像并转换为PNG
                    with Image.open(webp_path) as img:
                        # 保留透明度通道（如果存在）
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGBA')
                        else:
                            img = img.convert('RGB')
                        img.save(png_path, 'PNG')
                    print(f"转换成功: {webp_path} -> {png_path}")
                except Exception as e:
                    print(f"转换失败 {webp_path}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将WebP图像转换为PNG格式')
    parser.add_argument('--folder', type=str, default='.',
                        help='要处理的文件夹路径（默认为当前目录）')
    
    args = parser.parse_args()
    target_folder = os.path.abspath(args.folder)
    
    print(f"开始转换文件夹: {target_folder}")
    convert_webp_to_png(target_folder)
    print("所有文件处理完成")