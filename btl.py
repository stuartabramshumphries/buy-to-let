#!/usr/bin/python
 
def main():
    ir = 0.04         # interest rates
    gr = 0.07         # property growth rate
    ltv = 0.75        # loan to value
    ib = 100000       # initial deposit/balance
    yrs = 10          # years to model
    startval = ival = ib/(1-ltv)
    for i in range(1,yrs+1):
        ival = ival *(1 + gr)
        if ival >= startval * 1.25:
 
        print "year     %d      val %.2f "  % ( i, ival)
 
 
if __name__ == '__main__':
    main()
