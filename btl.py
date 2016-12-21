#!/usr/bin/python
# -*- coding: utf-8 -*-
# need to add more info here for other users or extend the README

__author__ = "Stuart Abrams-Humphries"
__email__ = "Stuart Abrams-Humphries (stuartabramshumphries@gmail.com)"
__maintainer__ = "Stuart Abrams-Humphries"
__license__ = "GPL"


def main():
    import os
    ir = 0.035                     # interest rate
    gr = 0.06                      # property growth rate
    ltv = 0.75                     # loan to value
    ib = 100000                    # initial deposit/balance
    yrs = 20                       # years to model
    yld = 0.04                     # rental yield
    mortgv = 0			   # initial mortgages
    savings = 0                    # amount added by savings
    startval = ib / (1.0 - ltv)    # initial price of property
    ival = startval
    yvals = []
    print startval
    for i in range(1, yrs + 1):
        ival += savings
        mortg = startval * ltv
        imortg = mortg
        ival *= (1.0 + gr)
        if ival >= startval *1.2:
            print 'remortgaging as value increased enough:'
            newfunds = ltv * (ival - startval)
            ival += newfunds / (1 - ltv)
            startval = ival
            mortg = startval * ltv
        rent = ival * yld - mortg * ir
        tax = (startval * yld - (0.2 * ir * mortg)) * 0.45  # this is using the new bad taxes - assuming worst case
        netrent = rent - tax
        ival += netrent
        yvals.append(ival)
        print 'year\t\t%d\t totval %d   netval %.2f rent %d netrent %d' % (i, ival,
                                                                           ival -mortg, rent, netrent)

    class Calgr(object):

        def __init__(self, ib, ival, yrs, ltv,imortg,savings):
            self.ib = ib
            self.ival = ival
            self.yrs = yrs
            self.ltv = ltv
            self.imortg = imortg
            self.savings = savings

        def irate(self):
            # trying to get what the ir is given initial balance and final balance
            from math import pow
            r = pow(((self.ival -self.imortg -self.savings*self.yrs)/ self.ib), 1.0 / self.yrs) - 1
            r *= 100
            return r

    vaal = Calgr(ib, ival, yrs, ltv,mortg,savings)
    valew = vaal.irate()
    print "Interest rate achieved is %.4f%%" % valew

    class Graphit(object):
    
        def __init__(self, xvals, yvals):
            self.xvals = xvals
            self.yvals = yvals

        def pretty(self):
            import matplotlib.pyplot as pyplot
            pyplot.title('portfolio growth over years')
            pyplot.xlabel('Years')
            pyplot.ylabel('portfolio value')
            pyplot.plot(xvals,yvals,color='blue',linestyle='dashed',label='total value')
            pyplot.savefig('./graph.png')
    xvals = range(0,yrs)
    graf = Graphit(xvals, yvals)
    graf.pretty()
    os.popen('(eog --new-instance ./graph.png)&')
if __name__ == '__main__':
    main()
