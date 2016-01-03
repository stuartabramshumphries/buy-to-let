#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    ir = 0.05  # interest rates
    gr = 0.03  # property growth rate
    ltv = 0.60  # loan to value
    ib = 140000  # initial deposit/balance
    yrs = 10  # years to model
    yld = 0.04  # rental yield
    savings = 0  # amount added by savings

    startval = ival = ib / (1 - ltv)
    for i in range(1, yrs + 1):
        ival += savings
        ival = ival * (1 + gr)
        if ival >= startval * (2 - ltv):
            print 'remortgaging as value increased enough:'
            newfunds = ltv * (ival - startval)
            ival = ival + newfunds / (1 - ltv)
        startval = ival
        rent = startval * yld - ltv * ir * startval
        tax = (startval * yld - (0.2*ltv * ir * startval))*0.45
        netrent = rent -tax
        ival = ival + netrent
        print 'year\t\t%d\t totval %d   val %.2f rent %d netrent %d' % (i, ival,
                ival * (1.0 - ltv),rent, netrent)

    class Calgr(object):
    
        def __init__(self,ib,ival,yrs,ltv):
            self.ib = ib
            self.ival = ival
            self.yrs = yrs
            self.ltv = ltv
    
        def irate(self):
        # trying to get what the ir is given initial balance and final balance
            from math import pow
            self.ival = self.ival * (1.0 - self.ltv)
            r = pow((self.ival/self.ib),1.0/self.yrs) -1
            r = r*100
            return r 

    vaal = Calgr(ib,ival,yrs,ltv) 
    valew = vaal.irate()
    print("Interest rate achieved is %.2f%%") % valew

if __name__ == '__main__':
    main()
