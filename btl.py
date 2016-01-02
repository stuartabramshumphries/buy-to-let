#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    ir = 0.03  # interest rates
    gr = 0.05  # property growth rate
    ltv = 0.75  # loan to value
    ib = 140000  # initial deposit/balance
    yrs = 20  # years to model
    yld = 0.05  # rental yield
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
    cal_gr(ib,ival,yrs,ltv)

def cal_gr(ib,ival,yrs,ltv):
    # trying to get what the ir is given initial balance and final balance
    from math import pow
    ival = ival * (1.0 - ltv)
    r = pow((ival/ib),1.0/yrs) -1
    r = r*100
    print "Your effective annual return is %0.2f percent" %  r

if __name__ == '__main__':
    main()
