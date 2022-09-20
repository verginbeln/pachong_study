from random import randint

import pygal


class Die():
    def __init__(self, num_sides=6):        #6面骰子
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)
if __name__ == '__main__':
    die = Die()
    results = []
    for roll_num in range(100):
        result = die.roll()
        results.append(result)
    print(results)

    frequencies = []
    for value in range(1,die.num_sides+1):
        frequency = results.count(value)     #列表.count计数
        frequencies.append(frequency)
    print(frequencies)                ###频率统计

    #########可视化
    hist = pygal.Bar()
    hist.title = "results of rolling one D6 1000 times"
    hist.x_labels = ["1","2","3","4","5","6"]
    hist.x_title = "result"
    hist.y_title = "Frequency of Result"

    hist.add("统计结果", frequencies)
    hist.render_to_file('die_visual.svg')



