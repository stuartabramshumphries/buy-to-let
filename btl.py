#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    ir = 0.04       # interest rates
    gr = 0.04       # property growth rate
    ltv = 0.75     # loan to value
    ib = 180000     # initial deposit/balance
    yrs = 20       # years to model
    yld = 0.0344      # rental yield
    savings = 0  # amount added by savings - note this messes up my interest rate achieved calc at the moment

    startval = ival = ib / (1 - ltv)
    mortg = startval * ltv
    for i in range(1, yrs + 1):
        ival += savings
        ival = ival * (1.0 + gr)
        if ival >= startval / ltv:
            print 'remortgaging as value increased enough:'
            newfunds = ltv * (ival - startval)
            ival = ival + newfunds / (1 - ltv)
            startval = ival
            mortg = startval * ltv
        rent = ival * yld - mortg * ir
        # this is using the new bad taxes - assuming worst case
        tax = (startval * yld - (0.2 * ir * mortg)) * 0.40
        netrent = rent - tax
        ival = ival + netrent
        print 'year\t\t%d\t totval %d   netval %.2f rent %d netrent %d' % (i, ival,
                                                                           ival * (1.0 - ltv), rent, netrent)

    class Calgr(object):

        def __init__(self, ib, ival, yrs, netval):
            self.ib = ib
            self.ival = ival
            self.yrs = yrs
            self.ltv = ltv
            self.netval = netval

        def irate(self):
            # trying to get what the ir is given initial balance and final
            # balance
            from math import pow
            r = pow((self.netval / self.ib), 1.0 / self.yrs) - 1
            r = r * 100
            return r

    netval = ival * (1.0 - ltv)
    vaal = Calgr(ib, ival, yrs, netval)
    valew = vaal.irate()
    print("Interest rate achieved is %.2f%%") % valew

if __name__ == '__main__':
    main()
