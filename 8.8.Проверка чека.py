final_summ = 0
count = []
check_data = input()
summary = check_data[4:].strip()
number_of_positions = check_data[0:4].strip()
for i in range(int(number_of_positions)):
    position = input()
    cost_of_item = int(position[0:7].strip())
    number_of_items = int(position[8:12].strip())
    summ_of_items = int(position[13:].strip())
    final_summ += number_of_items * cost_of_item
    print(final_summ)
    if summ_of_items == number_of_items * cost_of_item:
        continue
    else:
        count.append(i + 1)

if final_summ != int(summary):
    print(int(summary) - final_summ)
    print(*count)
else:
    print(0)