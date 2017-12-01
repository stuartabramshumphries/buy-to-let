 #!/usr/bin/python
# -*- coding: utf-8 -*-
# need to add more info here for other users or extend the README

__author__      = "Stuart Abrams-Humphries"
__email__       = "Stuart Abrams-Humphries (stuartabramshumphries@gmail.com)"
__maintainer__  = "Stuart Abrams-Humphries"
__license__     = "GPL"


def main():
    import os
    import sys
    def read_data():
        with open("./data.in") as fin:
            for val in fin.readlines():
                if '#' in val:
                    pass
                else:
                    return map(float,val.split())
    (ir,gr,ltv,dep,yrs,retrn,savings) = read_data()
    yrs = int(yrs)
    startval = dep / (1.0 - ltv)    # initial price of property
    ival = startval
    yvals = []
    yvals2 = []
    for i in range(1, int(yrs) + 1):
        ival += savings
        mortg = startval * ltv
        ival *= (1.0 + gr)
        if ival - 50000 >= startval:
            print 'remortgaging as value increased enough:'
            newfunds = ltv * (ival - startval)
            ival += newfunds / (1 - ltv)
            startval = ival
            mortg = startval * ltv
        rent = ival * retrn - mortg * ir
    # this is using the new bad taxes - assuming worst case
      #  tax = (startval * retrn - (0.2 * ir * mortg)) * 0.45
        tax = (startval * retrn - (ir * mortg)) * 0.20
        netrent = rent - tax
        ival += netrent
        yvals.append(ival)
        yvals2.append(ival - mortg)
        print 'year\t\t%d\t totval %d   netval %.2f rent %d netrent %d' % (i, ival,
                                                                           ival - mortg, rent, netrent)

    class Calgr(object):

        def __init__(self, dep, ival, yrs, ltv, imortg, savings):
            self.dep = dep
            self.ival = ival
            self.yrs = yrs
            self.ltv = ltv
            self.imortg = imortg
            self.savings = savings

        def irate(self):
            # trying to get what the ir is given initial balance and final
            # balance
            from math import pow
            r = pow(
                ((self.ival - self.imortg - self.savings * self.yrs) / self.dep),
                1.0 / self.yrs) - 1
            r *= 100
            return r

    vaal = Calgr(dep, ival, yrs, ltv, mortg, savings)
    valew = vaal.irate()
    print "Interest rate achieved is %.4f%%" % valew

    class Graphit(object):

        def __init__(self, xvals, yvals, yvals2):
            self.xvals = xvals
            self.yvals = yvals
            self.yvals2 = yvals2

        def pretty(self):
            import matplotlib.pyplot as pyplot
            fig_size = pyplot.rcParams["figure.figsize"]
            fig_size[0] = 15.0
            fig_size[1] = 15.0
            pyplot.rcParams["figure.figsize"] = fig_size
            pyplot.title('portfolio growth over yrs')
            pyplot.xlabel('Years')
            pyplot.ylabel('portfolio value')
            pyplot.plot(
                xvals,
                yvals,
                color='blue',
                linestyle='dashed',
                label='total value',
                linewidth=5.0)
            pyplot.plot(
                xvals,
                yvals2,
                color='green',
                linestyle='dashed',
                label='net value',
                linewidth=5.0)
            pyplot.legend(loc='upper left')
            pyplot.savefig('./graph.png')

    if len(sys.argv) > 1:
        if sys.argv[1] == "graph":
            xvals = range(0, yrs)
            graf = Graphit(xvals, yvals, yvals2)
            graf.pretty()
            os.popen('(open ./graph.png)&')

if __name__ == '__main__':
    main()
