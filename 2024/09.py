from __future__ import annotations
content = open('data.txt').read()
#content = '2333133121414131402'

def get_blocks():
    nums = [int(i) for i in content]
    blocks = []
    for i in range(0, len(nums)):
        if nums[i] > 0: 
            blocks.append([i//2 if i % 2 == 0 else None, nums[i]])
    return blocks

def reorder_blocks(blocks, part: int):
    file_idx = len(blocks) - 1
    while file_idx >= 0: 
        file_id, file_size = blocks[file_idx]
        if file_id == None or file_size == 0:
            file_idx -= 1
            continue
            
        empty_idx = None
        for i, (block_id, block_size) in enumerate(blocks[:file_idx]):
            if (block_id is None and block_size > 0) and (part == 1 or block_size >= file_size):
                empty_idx = i
                break
        if empty_idx is None:
            file_idx -= 1
            continue
        empty_size = blocks[empty_idx][1]
        put_size = min(file_size, empty_size)
        blocks[empty_idx][1] -= put_size
        blocks[file_idx][1] -= put_size
        blocks.insert(file_idx, [None, put_size])
        blocks.insert(empty_idx, [file_id, put_size])
        file_idx += 2

    return blocks

def compute_checksum(blocks):
    idx = 0
    checksum = 0
    for file_id, file_size in blocks:
        file_id = 0 if file_id is None else file_id
        for _ in range(file_size):
            checksum += idx * file_id
            idx += 1
    return checksum

print(compute_checksum(reorder_blocks(get_blocks(), 1)))
print(compute_checksum(reorder_blocks(get_blocks(), 2)))