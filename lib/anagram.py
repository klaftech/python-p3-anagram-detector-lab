class Anagram:
    def __init__(self,target):
        self.target = sorted(target)
        self.matches = []

    def match(self,list):
        for option in list:
            if sorted(option) == self.target:
                self.matches.append(option)
        print(self.matches)
        return self.matches

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
# => ['inlets']