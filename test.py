import os

def convert_filenames_to_lower(target_dir):
    # 验证目标文件夹是否存在
    if not os.path.exists(target_dir):
        print(f"错误：目标文件夹不存在 -> {target_dir}")
        return

    # 递归遍历文件夹（包括子文件夹）
    for root, dirs, files in os.walk(target_dir):
        # 1. 处理文件（文件名大写转小写）
        for filename in files:
            # 跳过已全小写的文件，避免重复操作
            if filename.islower():
                continue
            
            # 构建旧文件完整路径和新文件名（全小写）
            old_file_path = os.path.join(root, filename)
            new_filename = filename.lower()
            new_file_path = os.path.join(root, new_filename)

            # 避免文件名冲突（若新文件名已存在，添加后缀避免覆盖）
            if os.path.exists(new_file_path):
                # 分离文件名和后缀（如 "Test.txt" -> ("Test", ".txt")）
                name_without_ext, ext = os.path.splitext(new_filename)
                suffix = 1
                # 循环生成不冲突的新文件名（如 "test_1.txt"）
                while os.path.exists(os.path.join(root, f"{name_without_ext}_{suffix}{ext}")):
                    suffix += 1
                new_file_path = os.path.join(root, f"{name_without_ext}_{suffix}{ext}")
                print(f"警告：{new_filename} 已存在，重命名为 {f'{name_without_ext}_{suffix}{ext}'}")

            # 执行重命名
            try:
                os.rename(old_file_path, new_file_path)
                print(f"成功：{old_file_path} -> {new_file_path}")
            except Exception as e:
                print(f"失败：{old_file_path} -> 重命名出错 - {str(e)}")

        # 2. 处理子文件夹（文件夹名也转为小写，可选关闭）
        for dirname in dirs:
            if dirname.islower():
                continue
            
            old_dir_path = os.path.join(root, dirname)
            new_dirname = dirname.lower()
            new_dir_path = os.path.join(root, new_dirname)

            # 文件夹名冲突处理
            if os.path.exists(new_dir_path):
                name_without_ext = new_dirname  # 文件夹无后缀，直接加后缀
                suffix = 1
                while os.path.exists(os.path.join(root, f"{name_without_ext}_{suffix}")):
                    suffix += 1
                new_dir_path = os.path.join(root, f"{name_without_ext}_{suffix}")
                print(f"警告：文件夹 {new_dirname} 已存在，重命名为 {f'{name_without_ext}_{suffix}'}")

            # 执行文件夹重命名
            try:
                os.rename(old_dir_path, new_dir_path)
                print(f"成功（文件夹）：{old_dir_path} -> {new_dir_path}")
            except Exception as e:
                print(f"失败（文件夹）：{old_dir_path} -> 重命名出错 - {str(e)}")

if __name__ == "__main__":
    # -------------------------- 请修改这里的目标文件夹路径 --------------------------
    # Windows 示例：r"C:\Users\YourName\Documents\TestFolder"（注意加 r 避免转义）
    # macOS/Linux 示例："/Users/YourName/Documents/TestFolder"
    TARGET_FOLDER = r"/Users/kerr/Documents/project/enlib/word"  # 替换为你的目标文件夹路径
    # ------------------------------------------------------------------------------

    # 执行转换
    convert_filenames_to_lower(TARGET_FOLDER)
    print("\n✅ 文件名小写转换完成！")
    