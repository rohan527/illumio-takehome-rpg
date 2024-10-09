import csv

class LogParser:
    @staticmethod
    def parse_logs(file_path):
        logs = []
        with open(file_path, 'r') as file:
            for line in file.readlines():
                log = line.strip().split()
                if log != []:
                    logs.append(log)
        return logs

    @staticmethod
    def parse_lookup(file_path):
        lookup_table = {}
        with open(file_path, 'r') as file:
            if file_path.endswith('.csv'):
                reader = csv.DictReader(file)
                for row in reader:
                    key = (row['dstport'], row['protocol'])
                    lookup_table[key] = row['tag']
            else:  # Assuming it's a TXT file
                for line in file.readlines():
                    temp = line.strip().split(',')
                    if len(temp) == 3:
                        dstport, protocol, tag = temp[0], temp[1], temp[2]
                        key = (dstport, protocol)
                        lookup_table[key] = tag
        return lookup_table