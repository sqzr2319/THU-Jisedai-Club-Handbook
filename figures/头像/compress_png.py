import os
import sys
from PIL import Image
import concurrent.futures

def compress_png(file_path):
    try:
        # 打开原始图像文件
        with Image.open(file_path) as img:
            # 创建临时文件名
            temp_path = file_path + ".tmp"
            
            # 使用优化和压缩保存为PNG
            img.save(
                temp_path,
                format="PNG",
                optimize=True,      # 启用优化
                compress_level=9,
                quantize=True   # 最高压缩级别 (0-9)
            )
            
            # 检查压缩效果
            original_size = os.path.getsize(file_path)
            compressed_size = os.path.getsize(temp_path)
            
            if compressed_size < original_size:
                # 删除原始文件并用压缩版本替换
                os.remove(file_path)
                os.rename(temp_path, file_path)
                print(f"压缩成功: {file_path} (节省: {original_size - compressed_size} 字节)")
                return True
            else:
                # 压缩没有减小文件大小，删除临时文件
                os.remove(temp_path)
                print(f"跳过: {file_path} (压缩后大小未减小)")
                return False
    except Exception as e:
        print(f"压缩失败 {file_path}: {str(e)}")
        return False

def main():
    # 收集所有PNG文件
    files_to_compress = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                files_to_compress.append(file_path)
    
    if not files_to_compress:
        print("未找到PNG图像文件")
        return
    
    print(f"找到 {len(files_to_compress)} 个PNG文件需要压缩")
    
    # 使用线程池并行处理压缩
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(compress_png, files_to_compress)
    
    success_count = sum(1 for result in results if result)
    print(f"压缩完成! 成功压缩: {success_count}/{len(files_to_compress)} 个文件")

if __name__ == "__main__":
    main()