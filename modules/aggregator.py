from collections import defaultdict
from modules.matcher import TagMatcher

class Aggregator:
    def __init__(self):
        self.tag_counts = defaultdict(int)
        self.port_protocol_counts = defaultdict(int)

    def aggregate(self, logs, matcher):
        for log in logs:
            tag = matcher.match_log_to_tag(log)
            self.tag_counts[tag] += 1
            port_protocol = (log[6], TagMatcher.PROTOCOL_MAP.get(log[7]))
            self.port_protocol_counts[port_protocol] += 1

    def get_results(self):
        return self.tag_counts, self.port_protocol_counts

    def write_results_to_files(self, tag_file, port_protocol_file):
        # Write tag counts to a file
        with open(tag_file, 'w') as tag_f:
            tag_f.write("Tag,Count\n")
            for tag, count in self.tag_counts.items():
                tag_f.write(f"{tag},{count}\n")
        
        # Write port/protocol counts to a file
        with open(port_protocol_file, 'w') as port_f:
            port_f.write("Port,Protocol,Count\n")
            for (port, protocol), count in self.port_protocol_counts.items():
                port_f.write(f"{port},{protocol},{count}\n")
