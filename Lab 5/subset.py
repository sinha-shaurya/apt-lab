# derive all subsets from  given set of numbers

class Nums:
    def __init__(self, params):
        params = list(set(params))
        self.list = params

    # generate all subsets
    def powerset(self, subset, index):
        # print current subset
        print(subset)
        for i in range(index, len(self.list)):

            subset.append(self.list[i])
            self.powerset(subset, i+1)
            # backtrack
            subset.pop(-1)
        return


l = list(map(int, input().split()))
n = Nums(l)
n.powerset([], 0)
