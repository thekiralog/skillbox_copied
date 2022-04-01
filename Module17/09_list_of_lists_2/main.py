nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nicest_list = [value for top_level_list in nice_list
               for mid_level_list in top_level_list
               for value in mid_level_list]

print(nicest_list)
