"""Testing the initial vertice calculation--first operation on the user input file"""

def calculate_first_vertices(dfd, zfd, Dc, hcc, wc, hc, hcd, lcd, psp):
    """Compute the first batch of vertices based on the user inputs
    Args:


    Returns:
    pt#i (double): General coordinate where x is the horizontal, z is vertical, and y is in/out of the domain

    """
    pt0x = 0
    pt0z = 0
    pt0y = 0

    pt1x = Dc # bottom right coord
    pt1z = 0
    pt1y = 0

    # Pt 2 is the bottom LHS secondary air inlet
    pt2x = 0
    pt2z = zfd - (dfd/2)
    pt2y = 0

    # Pt 3 is the bottom RHS secondary air inlet
    pt3x = Dc
    pt3z = zfd- (dfd/2)
    pt3y = 0

    # pt4 is RHS top of secondary air inlet
    pt4x = Dc
    pt4z = zfd + (dfd/2)
    pt4y = 0

    # pt5 is the left hand side top of secondary air inlet
    pt5x = 0
    pt5z = zfd + (dfd/2)
    pt5y = 0

    # pt 6 is LHS chamber to cone deck
    pt6x = 0
    pt6y = 0
    pt6z = hcd # cone deck Height

    # pt 7 is RHS chamber to cone deck
    pt7x = Dc
    pt7y = 0
    pt7z = hcd # cone deck Height

    # pt 8 is RHS bottom of Channel
    pt8x = Dc + lcd # chamber diam plus length cone deck
    pt8z = hcd
    pt8y = 0

    # pt9 is LHS left bottom channel
    pt9x = -1*lcd
    pt9z = hcd
    pt9y = 0

    # pt10 is LHS top left channel
    pt10x = -1*lcd
    pt10z = hc + hcd # channel height plus height of cone deck
    pt10y = 0

    # pt 11 is LHS top right channel
    pt11x = -1*lcd + wc
    pt11z = hc + hcd
    pt11y = 0

    # pt 12 is RHS top right channel
    pt12x = Dc + (lcd-wc)
    pt12z = hc + hcd
    pt12y = 0

    # pt13 is RHS top right channel
    pt13x = Dc + lcd
    pt13z = hc + hcd
    pt13y = 0

    # pt14 is LHS bottom inner channel wall
    pt14x = -1*lcd + wc
    pt14z = hcd + psp
    pt14y = 0

    #pt 15 is RHS bottom inner channel wall
    pt15x = Dc + (lcd-wc)
    pt15z = hcd + psp
    pt15y = 0

    # Convert the Q_100 to flow velocity:
    A_secondary = 3.1415923*(dfd**2) # Area of circle
    U_100 = Q_100*A_secondary
    Q_100 = U_100 # Reassign

    return pt0x, pt0z, pt0y, pt1x, pt1z, pt1y, pt2x, pt2z, pt2y, pt3x, pt3z, pt3y, pt4x, pt4z, pt4y, pt5x, pt5z, pt5y, pt6x, pt6z, pt6y, pt7x, pt7z, pt7y, pt8x, pt8z, pt8y, pt9x, pt9z, pt9y, pt10x, pt10z, pt10y, pt11x, pt11z, pt11y, pt12x, pt12z, pt12y, pt13x, pt13z, pt13y,  pt14x, pt14z, pt14y, pt15x, pt15z, pt15y, Q_100


def test_calculate_first_vertices():
    """Testing the calculate_first_vertices fn"""
    dfd = 0 # forced draft diameter
    zfd = 0
    Dc = 0
    hcc = 0
    wc = 0
    hc = 0
    hcd = 0
    lcd = 0
    psp = 0
