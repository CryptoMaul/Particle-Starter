import math


def muonData(pt, eta, phi, m = 0.1):
    theta = 2*math.atan(math.e**(-eta))
    px = pt*math.cos(phi)
    py = pt*math.cos(phi)
    pz = pt*(1/math.tan(theta))

    p = (px**2+py**2+pz**2)**0.5
    energy = (m**2 + p**2)**0.5
    fVector = [energy, px, py, pz]

    return [energy, p, fVector]


def invMass(m1, m2, run, event):
    e1 = m1[0]
    e2 = m2[0]
    p1 = m1[1]
    p2 = m2[1]
    fV1 = m1[2]
    fV2 = m2[2]
    return [run, event, fV1, fV2, ((e1 + e2)**2 - math.fabs(p1 + p2)**2)**0.5]


print(invMass(muonData(231.277, 0.496237, -2.22082), muonData(222.408, -0.198471, 0.942319), 141544, 5))
