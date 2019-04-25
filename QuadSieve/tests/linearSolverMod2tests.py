import sys
sys.path.append("..")
import linearSolverMod2



def testNoSolution():
    passed=linearSolverMod2.solve([[1,1,0,1,0,0],[1,0,1,0,1,0],[0,1,1,0,0,1]])==[]
    if passed:
        print("passed testNoSolution")
    return passed

def testMatrixInPaper():
    passed=linearSolverMod2.solve([[1,1,0,0],[1,1,0,1],[0,1,1,1],[0,0,1,0],[0,0,0,1]])==[{0,4,1}]
    if passed:
        print("passed testNoSolution")
    return passed

def testMatrixInPaperRearranged():
    passed=linearSolverMod2.solve([[0,1,1,1],[0,0,0,1],[1,1,0,0],[0,0,1,0],[1,1,0,1]])==[{1,2,4}]
    if passed:
        print("passed testMatrixInPaperRearranged")
    return passed

def testTwoPairs():
    """
    primes: 2,3,5,7,11,13

    12 = (2,1,0,0,0,0)
    75 = (0,1,2,0,0,0)
    539 = (0,0,0,2,1,0)
    1859 = (0,0,0,0,1,2)
    """
    passed=linearSolverMod2.solve([[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0]])==[{0,1},{2,3}]
    if passed:
        print("passed testTwoPairs")
    return passed

def testMultipleSolutions():
    """
    primes: 2,3

    2 = (1,0)
    3 = (0,1)
    8 = (3,0)
    32 = (5,0)
    """
    passed=linearSolverMod2.solve([[1,0],[0,1],[1,0],[1,0]])
    print(passed)
    return False

testFunctions=[testNoSolution,testMatrixInPaper,testMatrixInPaperRearranged,testTwoPairs,testMultipleSolutions]

def runAllTests():
    numpassed=0
    for test in testFunctions:
        numpassed+=test()  
    print("passed "+str(numpassed)+"/"+str(len(testFunctions))+" tests")

runAllTests();
