from PIL import Image
import os
import glob

# 目标尺寸
TARGET_SIZE = (128, 128)

# 创建输出目录
output_dir = 'resized_images'
os.makedirs(output_dir, exist_ok=True)

# 支持的图片格式
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif']

# 获取所有图片文件
image_files = []
for ext in image_extensions:
    image_files.extend(glob.glob(ext))

print(f"找到 {len(image_files)} 张图片需要处理")

# 处理每张图片
for img_path in image_files:
    try:
        with Image.open(img_path) as img:
            # 保持原始宽高比进行缩放
            img.thumbnail(TARGET_SIZE, Image.LANCZOS)
            
            # 创建128x128新图像
            new_img = Image.new('RGB', TARGET_SIZE, (255, 255, 255))
            
            # 计算居中位置
            x = (TARGET_SIZE[0] - img.width) // 2
            y = (TARGET_SIZE[1] - img.height) // 2
            
            # 粘贴缩放后的图像
            new_img.paste(img, (x, y))
            
            # 保存结果
            filename = os.path.basename(img_path)
            output_path = os.path.join(output_dir, filename)
            new_img.save(output_path)
            print(f"已处理: {filename} -> {output_path}")
            
    except Exception as e:
        print(f"处理 {img_path} 时出错: {str(e)}")

print("所有图片处理完成！")