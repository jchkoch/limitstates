"""
Tests if sections load properly for CSA o86
"""

import pytest

# from limitstates import MaterialElastic, SectionRectangle
# import limitstates.design.csa.o86.c19 as o86


import limitstates as ls
import limitstates.design.csa.o86.c19 as o86

mm = 0.001
m = 1
MPa = 1
width = 356
depth = 600
Length = 6*m

matDict = {'E':9500*MPa, 'fb':25*MPa}
myMat       = o86.MaterialGlulamCSA19(matDict)
mySection   = ls.SectionRectangle(myMat, width, depth)   
line = ls.getLineFromLength(Length, 'm')

def test_GlulamInits():
    """
    Checks if the glulam element initializes and has the right attributes.

    Returns
    -------
    None.

    """
    myElement = o86.GlulamBeamColumnCSA19(line, mySection, 'm')
    
    assert hasattr(myElement.designProps, 'firePortection')
    assert hasattr(myElement.designProps, 'fireSection')


def test_getGlulamBeamColumn():
    """
    Checks if the glulam element initializes and has the right attributes.

    Returns
    -------
    None.

    """

    myElement = o86.getBeamColumnGlulamCSA19(Length, mySection, 'm')
        
    assert hasattr(myElement.designProps, 'firePortection')
    assert hasattr(myElement.designProps, 'fireSection')

 
# myMat = ls.MaterialElastic(9.5*1000)

# sections = getRectangularSections(myMat, 'csa', 'glulam', 'csa-19.csv')
if __name__ == "__main__":
    test_GlulamInits()
    test_getGlulamBeamColumn()