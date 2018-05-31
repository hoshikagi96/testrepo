from random import choice
import re

class Responder:

    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary
    
    def response(self, *args):
        pass

    @property
    def name(self):
        return self._name


class WhatResponder(Responder):
# AIの応答を制御。 ｘｘってなに？と返す    
    def response(self, text):
        return "{}ってなに？".format(text)

class PatternResponder(Responder):
    
    def response(self, text):
        for ptn in self._dictionary.pattern:
            matcher = re.match(ptn["pattern"], text)
            if matcher:
                chosen_response = choice(ptn["phrases"])
                return chosen_response.replase("%match%", matcher[0])
            return choice(self._dictionary.random)

class RandomResponder(Responder):
# AIの応答を制御。 登録された文字列からランダムに
    # def __init__(self, name):
    #     super().__init__(name)
    #     self._responses = []
    #     with open("dics/random.txt", encoding="utf-8") as f:
    #         for line in f:
    #             if line:
    #                 line = line.strip()
    #                 # 改行文字列を削除
    #                 self._responses.append(line)
    
    def response(self, _):
        return choice(self._dictionary)
   
