#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    ir = 0.04       # interest rates
    gr = 0.05       # property growth rate
    ltv = 0.75     # loan to value
    ib = 180000     # initial deposit/balance
    yrs = 10       # years to model
    yld = 0.04      # rental yield
    savings = 0  # amount added by savings - note this messes up my interest rate achieved calc at the moment

    startval = ival = ib / (1 - ltv)
    for i in range(1, yrs + 1):
        ival += savings
        mortg = startval * ltv
        ival = ival * (1.0 + gr)
        if ival >= startval / ltv:
            print 'remortgaging as value increased enough:'
            newfunds = ltv * (ival - startval)
            ival = ival + newfunds / (1 - ltv)
            startval = ival
            mortg = startval * ltv
        rent = ival * yld - mortg * ir
        # this is using the new bad taxes - assuming worst case
        tax = (startval * yld - (0.2 * ir * mortg)) * 0.45
        netrent = rent - tax
        ival = ival + netrent
        print 'year\t\t%d\t totval %d   netval %.2f rent %d netrent %d' % (i, ival,
                                                                           ival * (1.0 - ltv), rent, netrent)

    class Calgr(object):

        def __init__(self, ib, ival, yrs, ltv):
            self.ib = ib
            self.ival = ival
            self.yrs = yrs
            self.ltv = ltv

        def irate(self):
            # trying to get what the ir is given initial balance and final
            # balance
            from math import pow
            self.ival = self.ival * (1.0 - self.ltv)
            r = pow((self.ival / self.ib), 1.0 / self.yrs) - 1
            r = r * 100
            return r

    vaal = Calgr(ib, ival, yrs, ltv)
    valew = vaal.irate()
    print("Interest rate achieved is %.2f%%") % valew

if __name__ == '__main__':
    main()
