import os
from PIL import Image
import concurrent.futures

def convert_to_png(file_path):
    try:
        # 打开原始图像文件
        with Image.open(file_path) as img:
            # 创建目标路径（相同路径，扩展名改为.png）
            png_path = os.path.splitext(file_path)[0] + '.png'
            
            # 转换并保存为PNG格式
            img.save(png_path, 'PNG')
            
            # 删除原始文件
            os.remove(file_path)
            
            print(f"转换成功: {file_path} -> {png_path}")
            return True
    except Exception as e:
        print(f"转换失败 {file_path}: {str(e)}")
        return False

def main():
    # 支持的图像格式
    valid_extensions = ('.jpg', '.jpeg', '.webp')
    
    # 收集所有需要转换的文件
    files_to_convert = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.lower().endswith(valid_extensions):
                file_path = os.path.join(root, file)
                files_to_convert.append(file_path)
    
    if not files_to_convert:
        print("未找到需要转换的图像文件")
        return
    
    print(f"找到 {len(files_to_convert)} 个需要转换的文件")
    
    # 使用线程池并行处理转换
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(convert_to_png, files_to_convert)
    
    success_count = sum(1 for result in results if result)
    print(f"转换完成! 成功: {success_count}/{len(files_to_convert)}")

if __name__ == "__main__":
    main()