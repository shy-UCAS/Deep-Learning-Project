import torch

# 检查PyTorch是否安装成功
print("PyTorch version:", torch.__version__)

# 检查CUDA是否可用
print("Is CUDA available:", torch.cuda.is_available())

# 如果CUDA可用，输出CUDA的版本信息
if torch.cuda.is_available():
    print("CUDA version:", torch.version.cuda)

    # 检查cuDNN是否可用
    print("cuDNN version:", torch.backends.cudnn.version())

    # 输出可用的CUDA设备数量
    print("Number of CUDA devices:", torch.cuda.device_count())

    # 输出当前使用的CUDA设备名称
    print("CUDA device name on this computeris :", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available.")
