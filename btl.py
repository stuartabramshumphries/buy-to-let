#!/usr/bin/python


def main():
    ir = 0.04         # interest rates
    gr = 0.05         # property growth rate
    ltv = 0.75        # loan to value
    ib = 160000       # initial deposit/balance
    yrs = 10          # years to model
    yld = 0.035
    startval = ival = ib/(1-ltv)
    for i in range(1, yrs+1):
        ival = ival * (1 + gr)
        if ival >= startval * (2-ltv):
            print "remo"
            newfunds = ltv * (ival - startval)
            ival = ival + (newfunds / (1 - ltv))
            startval = ival
        rent = startval*yld -ltv*ir*startval
        ival = ival + rent
        print "year\t\t%d\t totval %d   val %.2f rent %d" % (i, ival, ival*(1.0 -ltv), rent)
        


if __name__ == '__main__':
    main()
