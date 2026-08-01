# Cumulative time for each note
time_on = [0] * 128

# Last 'on' time for each note. -1 means that the note isn't on
last_on = [-1] * 128


def map_line(line):
    # turn a line from the data file into a tuple
    (_, timestamp, status, _, note, _) = line.split(',')
    return (
        int(timestamp),
        status.strip() == 'Note_on_c',
        int(note)
        )


data_file = open('data.dat', 'r')
data = [map_line(line) for line in data_file.readlines()]
data_file.close()

# data.sort() Removing data sort as per suggestion

for (time, note_on, note) in data:
    if note_on and last_on[note] == -1:
        last_on[note] = time
    elif not note_on and last_on[note] != -1:
        time_on[note] += time - last_on[note]
        last_on[note] = -1

# Handle cases where notes are still on at the end of the file
for i in range(128):
    if last_on[i] != -1:
        time_on[i] += data[-1][0] - last_on[i]  # Add time until the last timestamp
        last_on[i] = -1 # Reset last on for consistency

for i in range(128):
    print('{}, {}'.format(i, time_on[i]))