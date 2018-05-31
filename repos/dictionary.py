class Dictionary:

    DICT_RANDOM = "dics/random.txt"
    DICT_PATTERN = "dics/pattern.txt"

    def __init__(self):
        with open(Dictionary.DICT_RANDOM, encoding="utf-8") as f:
            self._random = [l for l in f.read().splitlines() if l]

        with open(Dictionary.DICT_PATTERN, encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

    @property
    def random(self):
            return self._random

    @property
    def pattern(self):
            return self._pattern

    @staticmethod
    def make_pattern(line):
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            # return {'pattern': pattern, 'phrases': phrases}           # 2017-10-09 修正
            return {'pattern': pattern, 'phrases': phrases.split('|')}