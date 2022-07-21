def hannoi_towers(disk, source, receiver, storage):
    if disk <= 0:
        return
    hannoi_towers(disk - 1, source, storage, receiver)
    print("Переложить диск", disk, "со стержня номер", source, "на стержень номер", receiver)
    hannoi_towers(disk - 1, storage, receiver, source)


disks_quantity = int(input('Введите количество дисков: '))
hannoi_towers(disks_quantity, '1', '3', '2')
