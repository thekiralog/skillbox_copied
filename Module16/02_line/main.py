fst_line = [height for height in range(160, 176, 2)]
scd_line = [height for height in range(162, 180, 3)]
common_line = fst_line + scd_line
iter_count = 0
while iter_count != len(common_line):
    for index, height in enumerate(common_line[::-1]):
        if height < common_line[index - 1]:

print(fst_line, scd_line, common_line)
