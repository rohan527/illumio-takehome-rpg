import os
from modules.matcher import TagMatcher

class FileUtils:
    @staticmethod
    def file_exists(file_path):
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0

class LogValidator:
    @staticmethod
    def is_valid_log(log):
        return len(log) == 14

    @staticmethod
    def is_valid_protocol(protocol_number):
        return protocol_number in TagMatcher.PROTOCOL_MAP.keys()
