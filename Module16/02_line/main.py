fst_line = [height for height in range(160, 176, 2)]
scd_line = [height for height in range(162, 180, 3)]
common_line = fst_line + scd_line
iter_count = 0
sorted(common_line)
print(fst_line, scd_line, common_line)
