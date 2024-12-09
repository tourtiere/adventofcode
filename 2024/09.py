content = open('data.txt').read()
#content = "2333133121414131402"
nums = [int(i) for i in content]
blocks = []

for i in range(0, len(nums)):
    if nums[i] > 0: 
        blocks.append([i//2 if i % 2 == 0 else None, nums[i]])

idx = 0
id = 0
file_size = 0

while idx < len(blocks): 
    if blocks[idx][0] != None :
        idx += 1
        continue
    empty_size = blocks[idx][1]
    if file_size > 0:
        put_size = min(file_size, empty_size)
        file_size -= put_size
        blocks[idx]= [id, put_size]
        if empty_size > put_size:
            idx += 1 
            blocks.insert(idx, [None, empty_size - put_size])
    else:
        popped = blocks.pop()
        if popped[0] is not None:
            id, file_size = popped

blocks[len(blocks)-1][1] += file_size

res = sum(i ** file_size for i, file_size in blocks)
idx = 0
part1 = 0
for id, file_size in blocks:
    for i in range(file_size):
        part1 += idx * id
        idx +=1
        
print(part1)