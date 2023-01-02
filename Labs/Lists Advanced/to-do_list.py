to_do_notes = []
while True:
    notes = input()
    if notes == 'End':
        break
    current_notes = notes.split('-')
    priority = int(current_notes[0])
    task = current_notes[1]
    to_do_notes.append((priority, task))

sorted_list = [task_data[1] for task_data in sorted(to_do_notes)]
print(sorted_list)




