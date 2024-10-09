import sys
from modules.parser import LogParser
from modules.matcher import TagMatcher
from modules.aggregator import Aggregator
from modules.utils import FileUtils, LogValidator

def main(log_file, lookup_file):

    if not FileUtils.file_exists(log_file) or not FileUtils.file_exists(lookup_file):
        print("Error: One or both input files are missing or empty.")
        return

    logs = LogParser.parse_logs(log_file)
    lookup_table = LogParser.parse_lookup(lookup_file)

    matcher = TagMatcher(lookup_table)
    aggregator = Aggregator()

    valid_logs = []

    for log in logs:
        if LogValidator.is_valid_log(log):
            if LogValidator.is_valid_protocol(log[7]):
                valid_logs.append(log)
            else:
                print(f"Invalid protocol number in log: {log}")
        else:
            print(f"Invalid log format: {log}")

    aggregator.aggregate(valid_logs, matcher)

    tag_counts, port_protocol_counts = aggregator.get_results()

    # Output the results
    print("\nTag Counts:")
    print("\nTag,Count ")
    for tag, count in tag_counts.items():
        print(f"\n{tag},{count}")

    print("\nPort/Protocol Combination Counts:")
    print("\nPort,Protocol,Count ")
    for (port, protocol), count in port_protocol_counts.items():
        print(f"\n{port},{protocol},{count}")

    aggregator.write_results_to_files('tag_counts.txt', 'port_protocol_counts.txt')

    print("\nResults saved to 'tag_counts.txt' and 'port_protocol_counts.txt'.")


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python main.py input/<log_file> input/<lookup_file>")
    else:
        main(sys.argv[1], sys.argv[2])
