import hashlib


def calculate_hash(file_path, hash_algorithm=hashlib.sha256):
    """计算文件的哈希值"""
    hasher = hash_algorithm()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def compare_files_by_hash(file1, file2):
    """通过哈希值比较两个文件是否相同"""
    hash1 = calculate_hash(file1)
    hash2 = calculate_hash(file2)
    return hash1 == hash2


# 示例用法
file1 = 'F:/nfsroot/dzfy_udp264_6To1_nnie_osd_0621'
file2 = 'C:/Users/21687/Desktop/dzfy_udp264_6To1_nnie_osd_0710'
if compare_files_by_hash(file1, file2):
    print("两个文件相同")
else:
    print("两个文件不同")
