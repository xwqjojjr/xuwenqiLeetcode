class Solution(object):
    def removeDuplicates(self, xs):
        if not xs:
            return 0
        w = 1
        for j, x in enumerate(xs[1:]):
            print j,xs[j],x
            if x != xs[j]:
                xs[w] = x
                w += 1
        return w