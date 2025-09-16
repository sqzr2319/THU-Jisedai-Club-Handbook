import os
from PIL import Image
import sys

def convert_png_to_jpg(path, compress=True, quality=85):
    """将PNG文件转换为JPG格式并替换原文件"""
    try:
        with Image.open(path) as img:
            # 处理透明背景（转换为白色背景）
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            elif img.mode == 'P':
                img = img.convert('RGB')
            
            # 保存为JPG并替换原文件
            jpg_path = os.path.splitext(path)[0] + '.jpg'
            img.save(jpg_path, 'JPEG', quality=quality if compress else 100)
            
            # 删除原始PNG文件
            os.remove(path)
            print(f"转换成功: {path} -> {jpg_path}")
            return True
    except Exception as e:
        print(f"处理文件 {path} 时出错: {str(e)}")
        return False

def main():
    # 设置是否启用压缩（True启用，False禁用）
    enable_compression = True
    
    # 设置压缩质量（仅当启用压缩时有效）
    compression_quality = 85  # 范围1-100，建议85-95
    
    # 获取当前脚本所在目录
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("开始转换PNG文件...")
    print(f"压缩模式: {'启用 (质量: ' + str(compression_quality) + ')' if enable_compression else '禁用'}")
    
    # 遍历所有子目录
    converted_count = 0
    error_count = 0
    
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.png'):
                file_path = os.path.join(foldername, filename)
                if convert_png_to_jpg(file_path, enable_compression, compression_quality):
                    converted_count += 1
                else:
                    error_count += 1
    
    print("\n转换完成!")
    print(f"成功转换文件数: {converted_count}")
    print(f"失败文件数: {error_count}")

if __name__ == "__main__":
    main()