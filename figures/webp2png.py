import os
from PIL import Image
import argparse

def convert_images_to_png():
    # 配置参数解析器
    parser = argparse.ArgumentParser(description='将图像文件转换为PNG格式')
    parser.add_argument('--input-dir', default=os.getcwd(), 
                       help='输入目录路径 (默认: 当前目录)')
    parser.add_argument('--output-dir', default=None,
                       help='输出目录路径 (默认: 同输入目录)')
    parser.add_argument('--quality', type=int, default=95,
                       help='PNG输出质量 (0-100, 默认:95)')
    parser.add_argument('--overwrite', action='store_true',
                       help='覆盖已存在的PNG文件')
    parser.add_argument('--formats', nargs='+', default=['webp', 'jpg', 'jpeg'],
                       help='要转换的格式 (默认: webp jpg jpeg)')
    # 添加删除原文件选项
    parser.add_argument('--delete-original', action='store_true',
                       help='转换成功后删除原始文件')
    args = parser.parse_args()

    # 设置输出目录
    output_dir = args.output_dir or args.input_dir
    os.makedirs(output_dir, exist_ok=True)
    
    # 支持的格式和对应扩展名
    supported_formats = {
        'webp': ('.webp',),
        'jpg': ('.jpg', '.jpeg'),  # 同时支持 .jpg 和 .jpeg
        'jpeg': ('.jpg', '.jpeg'),  # 添加 jpeg 作为有效格式标识符
        'png': ('.png',),
        'bmp': ('.bmp',),
        'gif': ('.gif',),
        'tiff': ('.tif', '.tiff')
    }
    
    # 获取所有目标扩展名
    target_exts = []
    for fmt in args.formats:
        fmt_lower = fmt.lower()  # 统一转换为小写
        
        # 检查格式是否支持
        if fmt_lower in supported_formats:
            target_exts.extend(supported_formats[fmt_lower])
        else:
            print(f"警告: 不支持的格式 '{fmt}' 将被忽略")
    
    if not target_exts:
        print("错误: 没有有效的转换格式")
        return
    
    # 转换计数器
    converted_count = 0
    skipped_count = 0
    deleted_count = 0
    
    # 遍历输入目录下的所有文件
    for filename in os.listdir(args.input_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        print(f"处理文件: {filename}")
        # 检查是否是需要转换的格式
        if file_ext not in target_exts:
            continue
            
        # 构建完整的文件路径
        input_path = os.path.join(args.input_dir, filename)
        
        # 生成输出文件名
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name + '.png')
        
        # 检查是否已存在PNG文件
        if not args.overwrite and os.path.exists(output_path):
            print(f"跳过 {filename}: PNG文件已存在")
            skipped_count += 1
            continue
            
        try:
            # 打开图像文件
            with Image.open(input_path) as img:
                # 创建输出目录结构
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # 转换模式
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGBA')
                else:
                    img = img.convert('RGB')
                
                # 保存为PNG格式
                img.save(output_path, 'PNG', quality=args.quality)
                converted_count += 1
                print(f"转换成功: {filename} -> {os.path.basename(output_path)}")
                
                # 添加删除原始文件功能
                if args.delete_original:
                    try:
                        os.remove(input_path)
                        deleted_count += 1
                        print(f"已删除原始文件: {filename}")
                    except Exception as e:
                        print(f"删除原始文件失败 {filename}: {str(e)}")
        
        except Exception as e:
            print(f"转换失败 {filename}: {str(e)}")
    
    # 打印总结报告
    print("\n转换完成!")
    print(f"成功转换: {converted_count} 个文件")
    print(f"删除原始文件: {deleted_count} 个文件")
    print(f"跳过: {skipped_count} 个文件")
    if args.output_dir:
        print(f"输出目录: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    convert_images_to_png()