#courtesy of https://www.reddit.com/r/adventofcode/comments/ebai4g/2019_day_16_solutions/fb5n79m/?context=3
#roughly a 0 percent chance I would have solved that on my own

from itertools import cycle, accumulate


s = '59773419794631560412886746550049210714854107066028081032096591759575145680294995770741204955183395640103527371801225795364363411455113236683168088750631442993123053909358252440339859092431844641600092736006758954422097244486920945182483159023820538645717611051770509314159895220529097322723261391627686997403783043710213655074108451646685558064317469095295303320622883691266307865809481566214524686422834824930414730886697237161697731339757655485312568793531202988525963494119232351266908405705634244498096660057021101738706453735025060225814133166491989584616948876879383198021336484629381888934600383957019607807995278899293254143523702000576897358'
offset = int(s[:7])
digits = [int(i) for i in s]


#we only care about the digits from the offset to the end
l = 10000 * len(digits) - offset
i = cycle(reversed(digits))
arr = [next(i) for _ in range(l)]

# Repeatedly take the partial sums mod 10
for _ in range(100):
    arr = [n % 10 for n in accumulate(arr)]

print("".join(str(i) for i in arr[-1:-9:-1]))