## @file test_All.py
#  @author Jay Mody
#  @brief Test driver for Set, MoleculeT, CompoundT, and ReactionT.
#  @date 08/02/20 (dd/mm/yy)

from Set import Set
from MoleculeT import MoleculeT
from CompoundT import CompoundT
from ReactionT import ReactionT
from ChemTypes import ElementT
from MolecSet import MolecSet
from ElmSet import ElmSet

import pytest
import numpy as np

# Set tests
def test_Set_init():
    assert Set([0, 1, 2])
    assert Set((0, "0", 1.2))

def test_Set_add():
    s = Set([1, 2, 3])

    s.add(12)
    assert s == Set([1, 2, 3, 12])

    s.add(3)
    assert s == Set([1, 2, 3, 12])

    s = Set([])

    s.add(1)
    assert s == Set([1])

    s.add("a")
    s.add("b")
    s.add("c")
    assert s == Set(["a", "b", "c", 1])

def test_Set_rm():
    with pytest.raises(ValueError):
        Set([]).rm(None)
    with pytest.raises(ValueError):
        Set([1]).rm(2)

    s = Set([1, 2, 3])
    s.rm(2)
    assert s == Set([1, 3])

    s = Set([1, 2, 3])
    s.rm(2)
    s.rm(1)
    s.rm(3)
    assert s == Set([])

def test_Set_member():
    assert not Set([]).member(True)
    assert not Set([1, 12, 2031]).member(-1)
    assert not Set([0.00001]).member(0)

    assert Set([1, 1, 1]).member(1)
    assert Set([1, 2, 3]).member(3)
    assert Set(["abc", 0]).member("abc")

def test_Set_size():
    assert Set([]).size() == 0
    assert Set([99]).size() == 1
    assert Set([1, 1, 1]).size() == 1
    assert Set(list(range(121))).size() == 121

def test_Set_equals():
    assert not Set([1, 2, 2012]).equals(Set([1, 2012]))
    assert not Set(["apple"]).equals(Set([]))

    assert Set([1, 2, 2012]).equals(Set([1, 2, 2012]))
    assert Set([1, 1, 1]).equals(Set([1]))


def test_Set_to_seq():
    assert isinstance(Set([1,2,3]).to_seq(), list)

    s = Set(list(range(2,20,3)))
    assert len(s.to_seq()) == s.size()


# MoleculeT tests
def test_MoleculeT_init():
    with pytest.raises(ValueError):
        MoleculeT(1, "He")
    with pytest.raises(ValueError):
        MoleculeT(0, ElementT.H)
    with pytest.raises(ValueError):
        MoleculeT(-1, ElementT.H)
    with pytest.raises(ValueError):
        MoleculeT(2.2, ElementT.He)

    assert MoleculeT(2, ElementT.H)
    assert MoleculeT(19999, ElementT.C)
    assert MoleculeT(1, ElementT.Fe)

def test_MoleculeT_get_num():
    assert MoleculeT(2, ElementT.O).get_num() == 2
    assert MoleculeT(1, ElementT.O).get_num() != 0

def test_MoleculeT_get_elm():
    assert MoleculeT(20, ElementT.O).get_elm() == ElementT.O
    assert MoleculeT(20, ElementT.H).get_elm() != 1

def test_MoleculeT_num_atoms():
    assert MoleculeT(20, ElementT.O).num_atoms(ElementT.O) == 20
    assert MoleculeT(10, ElementT.H).num_atoms(ElementT.O) == 0

def test_MoleculeT_constit_elems():
    assert MoleculeT(2, ElementT.H).constit_elems() == MoleculeT(1, ElementT.H).constit_elems()
    assert MoleculeT(3, ElementT.Mg).constit_elems() == ElmSet([ElementT.Mg])

def test_MoleculeT_equals():
    assert MoleculeT(2, ElementT.H).equals(MoleculeT(2, ElementT.H))
    assert MoleculeT(19999, ElementT.C) == MoleculeT(19999, ElementT.C)


# CompoundT tests
def test_CompoundT_init():
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(1, ElementT.O)

    with pytest.raises(ValueError):
        CompoundT([m1, m2])
    with pytest.raises(ValueError):
        CompoundT(set([m1, m2]))

    s = MolecSet([m1, m2])
    assert CompoundT(s)
    assert CompoundT(MolecSet([]))

def test_CompoundT_get_molec_set():
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(1, ElementT.O)
    s1 = MolecSet([m1, m2])

    m3 = MoleculeT(2, ElementT.H)
    m4 = MoleculeT(1, ElementT.O)
    s2 = MolecSet([m3, m4])

    c = CompoundT(s1)
    assert c.get_molec_set() == s2

    s1.add(MoleculeT(1, ElementT.He))
    print(s1.size())
    print(c.get_molec_set().size())
    assert c.get_molec_set() != s1

def test_CompoundT_num_atoms():
    m1 = MoleculeT(22, ElementT.H)
    m2 = MoleculeT(1, ElementT.O)
    m3 = MoleculeT(1, ElementT.O)
    c = CompoundT(MolecSet([m1, m2, m3]))
    assert c.num_atoms(ElementT.H) == 22
    assert c.num_atoms(ElementT.O) == 1
    assert c.num_atoms(ElementT.He) == 0

    m1 = MoleculeT(1, ElementT.Na)
    m2 = MoleculeT(1, ElementT.Cl)
    c = CompoundT(MolecSet([m1, m2]))
    assert c.num_atoms(ElementT.Na) == 1
    assert c.num_atoms(ElementT.Cl) == 1
    assert c.num_atoms(ElementT.H) == 0

def test_CompoundT_constit_elems():
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(1, ElementT.O)
    c = CompoundT(MolecSet([m1, m2]))
    assert c.constit_elems() == ElmSet([ElementT.H, ElementT.O])

    m1 = MoleculeT(1, ElementT.Na)
    m2 = MoleculeT(1, ElementT.Cl)
    c = CompoundT(MolecSet([m1, m2]))
    assert c.constit_elems() != ElmSet([ElementT.Na, ElementT.C])

def test_CompoundT_equals():
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(1, ElementT.O)
    s1 = MolecSet([m2, m1])

    m3 = MoleculeT(2, ElementT.H)
    m4 = MoleculeT(1, ElementT.O)
    s2 = MolecSet([m3, m4])

    assert CompoundT(s1) == CompoundT(s2)

    s2.add(MoleculeT(42, ElementT.U))
    assert CompoundT(s1) != CompoundT(s2)


# ReactionT tests
## @cite https://www.nayuki.io/page/chemical-equation-balancer-javascript
def test_ReactionT_init():
    # HClFe -> NO, is an invalid chemical equation
    m1 = MoleculeT(1, ElementT.H)
    m2 = MoleculeT(1, ElementT.Cl)
    m3 = MoleculeT(1, ElementT.Fe)
    m4 = MoleculeT(1, ElementT.N)
    m5 = MoleculeT(1, ElementT.O)
    lhs = [CompoundT(MolecSet([m1, m2, m3]))]
    rhs = [CompoundT(MolecSet([m4, m5]))]

    with pytest.raises(Exception):
        ReactionT(lhs, rhs)

    # H2 + O2 -> H2O, is a valid chemical equation that can be balanced
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(2, ElementT.O)
    m3 = MoleculeT(1, ElementT.O)
    lhs = [
        CompoundT(MolecSet([m1])),
        CompoundT(MolecSet([m2])),
    ]
    rhs = [
        CompoundT(MolecSet([m1, m3]))
    ]

    assert ReactionT(lhs, rhs)

def test_ReactionT_get_lhs():
    # H2 + O2 -> H2O
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(2, ElementT.O)
    m3 = MoleculeT(1, ElementT.O)
    lhs = [
        CompoundT(MolecSet([m1])),
        CompoundT(MolecSet([m2])),
    ]
    rhs = [
        CompoundT(MolecSet([m1, m3]))
    ]

    assert ReactionT(lhs, rhs).get_lhs() == lhs

def test_ReactionT_get_rhs():
    # H2 + O2 -> H2O
    m1 = MoleculeT(2, ElementT.H)
    m2 = MoleculeT(2, ElementT.O)
    m3 = MoleculeT(1, ElementT.O)
    lhs = [
        CompoundT(MolecSet([m1])),
        CompoundT(MolecSet([m2])),
    ]
    rhs = [
        CompoundT(MolecSet([m1, m3]))
    ]

    assert ReactionT(lhs, rhs).get_rhs() == rhs

def test_ReactionT_get_lhs_coeff():
    # H2 + O2 -> H20, coeffs [2, 1, 2]
    h2 = MoleculeT(2, ElementT.H)
    o2 = MoleculeT(2, ElementT.O)
    o1 = MoleculeT(1, ElementT.O)
    lhs = [
        CompoundT(MolecSet([h2])),
        CompoundT(MolecSet([o2])),
    ]
    rhs = [
        CompoundT(MolecSet([h2, o1]))
    ]
    assert ReactionT(lhs, rhs).get_lhs_coeff() == [2, 1]

    # Mg(OH)2 -> MgO + H20, coeffs [1, 1, 1]
    mg1 = MoleculeT(1, ElementT.Mg)
    lhs = [
        CompoundT(MolecSet([mg1, h2, o2])),
    ]
    rhs = [
        CompoundT(MolecSet([mg1, o1])),
        CompoundT(MolecSet([h2, o1]))
    ]
    assert ReactionT(lhs, rhs).get_lhs_coeff() == [1]

    # Mg(OH)2 -> MgO + H20, coeffs [2, 3, 4, 3]
    fe2 = MoleculeT(2, ElementT.Fe)
    fe1 = MoleculeT(1, ElementT.Fe)
    o3 = MoleculeT(3, ElementT.O)
    c1 = MoleculeT(1, ElementT.C)
    lhs = [
        CompoundT(MolecSet([fe2, o3])),
        CompoundT(MolecSet([c1])),
    ]
    rhs = [
        CompoundT(MolecSet([fe1])),
        CompoundT(MolecSet([c1, o2]))
    ]
    assert ReactionT(lhs, rhs).get_lhs_coeff() == [2, 3]

def test_ReactionT_get_rhs_coeff():
    # H2 + O2 -> H20, coeffs [2, 1, 2]
    h2 = MoleculeT(2, ElementT.H)
    o2 = MoleculeT(2, ElementT.O)
    o1 = MoleculeT(1, ElementT.O)
    lhs = [
        CompoundT(MolecSet([h2])),
        CompoundT(MolecSet([o2])),
    ]
    rhs = [
        CompoundT(MolecSet([h2, o1]))
    ]
    assert ReactionT(lhs, rhs).get_rhs_coeff() == [2]

    # Mg(OH)2 -> MgO + H20, coeffs [1, 1, 1]
    mg1 = MoleculeT(1, ElementT.Mg)
    lhs = [
        CompoundT(MolecSet([mg1, h2, o2])),
    ]
    rhs = [
        CompoundT(MolecSet([mg1, o1])),
        CompoundT(MolecSet([h2, o1]))
    ]
    assert ReactionT(lhs, rhs).get_rhs_coeff() == [1, 1]

    # Mg(OH)2 -> MgO + H20, coeffs [2, 3, 4, 3]
    fe2 = MoleculeT(2, ElementT.Fe)
    fe1 = MoleculeT(1, ElementT.Fe)
    o3 = MoleculeT(3, ElementT.O)
    c1 = MoleculeT(1, ElementT.C)
    lhs = [
        CompoundT(MolecSet([fe2, o3])),
        CompoundT(MolecSet([c1])),
    ]
    rhs = [
        CompoundT(MolecSet([fe1])),
        CompoundT(MolecSet([c1, o2]))
    ]
    assert ReactionT(lhs, rhs).get_rhs_coeff() == [4, 3]
