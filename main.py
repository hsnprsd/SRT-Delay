import re
from datetime import timedelta, datetime
import argparse

def move_srt(from_file, to_file, delay):
    out_lines = []
    with open(from_file, 'r') as f:
        in_lines = f.readlines()
        for line in in_lines:
            times = line.strip().split(' --> ')
            if len(times) != 2:
                out_lines.append(line)
                continue
            from_time = datetime.strptime(times[0], '%H:%M:%S,%f')
            to_time = datetime.strptime(times[1], '%H:%M:%S,%f')
            from_time += timedelta(seconds=delay)
            to_time += timedelta(seconds=delay)
            out_lines.append(f"{from_time.strftime('%H:%M:%S,000')} --> {to_time.strftime('%H:%M:%S,000')}\n")
    with open(to_file, 'w') as f:
        f.writelines(out_lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Delay srt")
    parser.add_argument('--input', type=str, default='in.srt')
    parser.add_argument('--output', type=str, default='out.srt')
    parser.add_argument('--delay', type=int, default=0, help="in seconds")
    args = parser.parse_args()

    move_srt(args.input, args.output, args.delay)

