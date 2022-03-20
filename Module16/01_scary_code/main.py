main_values = [1, 5, 3]
scd_values = [1, 5, 1, 5]
trd_values = [1, 3, 1, 5, 3, 3]
for i_val in scd_values:
    main_values.append(i_val)
print('Количество цифр 5 при первом объединении:', main_values.count(5))
for i_val in main_values:
    if i_val == 5:
        main_values.remove(i_val)
for i_val in trd_values:
    main_values.append(i_val)
print('Количество цифр 3 при втором объединении:', main_values.count(3))
print(main_values)
