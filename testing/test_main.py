import unittest
from modules.matcher import TagMatcher
from modules.aggregator import Aggregator
from modules.utils import LogValidator

class TestFlowLogs(unittest.TestCase):

    def setUp(self):
        self.lookup_table = {
            ('443', 'tcp'): 'sv_P2',
            ('25', 'tcp'): 'sv_P1'
        }
        self.logs = [
            ['2', '123', 'eni-xyz', '10.0.1.1', '198.51.100.1', '443', '49153', '6', '25', '2000', '1620140761', '1620140821', 'ACCEPT', 'OK'],
            ['2', '123', 'eni-abc', '10.0.1.2', '198.51.100.2', '25', '49154', '6', '25', '2000', '1620140761', '1620140821', 'ACCEPT', 'OK']
        ]

    def test_tag_matching(self):
        matcher = TagMatcher(self.lookup_table)
        tag1 = matcher.match_log_to_tag(self.logs[0])
        tag2 = matcher.match_log_to_tag(self.logs[1])
        self.assertEqual(tag1, 'sv_P2')
        self.assertEqual(tag2, 'sv_P1')

    def test_aggregation(self):
        matcher = TagMatcher(self.lookup_table)
        aggregator = Aggregator()
        aggregator.aggregate(self.logs, matcher)

        tag_counts, port_protocol_counts = aggregator.get_results()

        self.assertEqual(tag_counts['sv_P2'], 1)
        self.assertEqual(tag_counts['sv_P1'], 1)
        self.assertEqual(port_protocol_counts[('443', 'tcp')], 1)
        self.assertEqual(port_protocol_counts[('25', 'tcp')], 1)

    def test_improper_log(self):
        ans = LogValidator.is_valid_log(self.logs[0][3:])
        self.assertEqual(False, ans)
    
    def test_proper_log(self):
        ans = LogValidator.is_valid_log(self.logs[0])
        self.assertEqual(True,ans)

    def test_invalid_protocol(self):
        ans = LogValidator.is_valid_protocol(self.logs[0][9])
        self.assertEqual(False, ans)

    def test_valid_protocol(self):
        ans = LogValidator.is_valid_protocol(self.logs[0][7])
        self.assertEqual(True, ans)


if __name__ == '__main__':
    unittest.main()
