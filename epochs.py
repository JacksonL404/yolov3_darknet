"""
关键参数解释和新的计算方法
batch size (bs): 每个批次中包含的图像数量（这里是16）。
accumulate: 累积的批次数（这里是4），表示每4个批次的梯度被累积后进行一次权重更新。
effective batch size: 实际的批量大小，等于批次大小乘以累积次数（16 * 4 = 64）。
"""

def calculate_epochs(total_batches, batch_size, accumulate, total_images):
    effective_batch_size = batch_size * accumulate
    effective_batches_per_epoch = total_images / effective_batch_size
    epochs = total_batches / effective_batches_per_epoch
    return epochs


total_batches = 500200
batch_size = 64
accumulate = 4
total_images = 12498

epochs = calculate_epochs(total_batches, batch_size, accumulate, total_images)
print(f"Total epochs: {epochs:.2f}")
