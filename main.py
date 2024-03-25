import heapq


def calculate(_cables):
    _cables = _cables[::1]
    costs = list()

    heapq.heapify(_cables)

    while len(_cables) > 1:
        cable1 = heapq.heappop(_cables)
        cable2 = heapq.heappop(_cables)
        total = cable1 + cable2

        costs.append(total)
        heapq.heappush(_cables, total)

    return costs


if __name__ == "__main__":
    cables = [55, 49, 63, 73, 83, 43, 53]
    costs = calculate(cables)

    print("Min cost: ", costs[0])
    print("Total costs: ", sum(costs))