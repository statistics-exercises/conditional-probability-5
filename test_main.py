import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_result(self) :
     mprior = sy.simplify("2*t")
     for mr in results : 
        if mr==1 : 
           mdenom = sy.integrate( t*mprior, (t,0,1) )
           mposterior = sy.simplify( t*mprior / mdenom )
        else : 
           mdenom = sy.integrate( (1-t)*mprior, (t,0,1) )
           mposterior = sy.simplify( (1-t)*mprior / mdenom )
        mprior = mposterior 
    self.assertTrue( mposterior==posterior, "your posterior distribution has not been calculated correctly" )
