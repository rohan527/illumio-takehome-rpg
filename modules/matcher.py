class TagMatcher:
    PROTOCOL_MAP = {
        '1': 'icmp',
        '4':'ipv4',
        '6': 'tcp',
        '17': 'udp',
        '2': 'igmp',
        '89': 'ospf',
        '118':'stp',
        '121':'smp',

        # Add other relevant protocol mappings as needed
    }

    def __init__(self, lookup_table):
        self.lookup_table = lookup_table

    def match_log_to_tag(self, log):
        dstport, protocol_number = log[6], log[7]
        protocol = self.PROTOCOL_MAP.get(protocol_number)

        if protocol is None:
            return 'Invalid Protocol'

        key = (dstport, protocol)
        return self.lookup_table.get(key, 'Untagged')
