import torch

print('CUDA available:', torch.cuda.is_available()) 
print('CUDA device count:', torch.cuda.device_count())
print('Current CUDA device:', torch.cuda.current_device())