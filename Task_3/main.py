import sys


def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return {}

    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    lines = list()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()

            for line in content:
                parsed_line = parse_log_line(line)
                lines.append(parsed_line)

    except FileNotFoundError:
        print(f"File salary.txt not found in {file_path}.")

    return lines


def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]


def count_logs_by_level(logs: list) -> dict:
    counts = dict()
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<15} | {'Кількість':<8}")
    print('-' * 17 + '|' + '-' * 10)

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        count = counts.get(level, 0)
        print(f"{level:<15} | {count:<8}")


def main():
    if len(sys.argv) < 1:
        print("Вкажіть шлях до файлу з логами")
        return
    if len(sys.argv) > 3:
        print("Некоректна команда")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        print("Логи відсутні")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        filter_level = sys.argv[2]

        filtered_logs = filter_logs_by_level(logs, filter_level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{filter_level.upper()}':")
            for log in filtered_logs:
                print(" ".join(log.values()))
        else:
            print(f"\n Логи з рівнем '{filter_level.upper()}' відсутні.")


if __name__ == '__main__':
    main()

#Command
# python ./Task_3/main.py ./Task_3/Logs.txt
# python ./Task_3/main.py ./Task_3/Logs.txt error