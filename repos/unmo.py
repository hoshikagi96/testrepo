import responder
from random import choice
from dictionary import Dictionary

class Unmo:
# 人工無能コアクラス

    def __init__(self, name):
    # 文字列を受け取り、コアインスタンスの名前に設定  
        self._dictionary = Dictionary()
        self._responders ={
            "what": responder.WhatResponder("What", self._dictionary),
            "random": responder.RandomResponder("Random", self._dictionary),
            # "pattern": responder.PatternResponder("Pattern", self._dictionary),
            }
        self._responder = self._responders["random"]
        self._name = name

    def dialogue(self, text):
        
        chosen_key = choice(list(self._responders.keys()))
        self._responder = self._responders[chosen_key]
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name

