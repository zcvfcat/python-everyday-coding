class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self) -> None:
        self.scoops = []

    def add_scoops(self, * new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) >= Bowl.max_scoops:
                break
            self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(one_scoop.flavor for one_scoop in self.scoops)

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3, s4)
b.add_scoops(s5)
print(b)