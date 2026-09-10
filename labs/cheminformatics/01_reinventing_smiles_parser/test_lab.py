"""
Unit Tests for Lab 01: Simple Molecule Parser
Run with: py scripts/runner.py test labs/cheminformatics/01_reinventing_smiles_parser/test_lab.py
"""

import unittest
from lab import SimpleMolecule

class TestSimpleMoleculeParser(unittest.TestCase):
    def test_single_atom(self):
        mol = SimpleMolecule("C")
        self.assertEqual(mol.atom_count(), 1)
        self.assertEqual(mol.bond_count(), 0)
        self.assertEqual(mol.atoms, ["C"])

    def test_linear_alkane(self):
        mol = SimpleMolecule("CCC") # Propane backbone
        self.assertEqual(mol.atom_count(), 3)
        self.assertEqual(mol.bond_count(), 2)
        self.assertEqual(mol.bonds, [(0, 1), (1, 2)])

    def test_heteroatoms(self):
        mol = SimpleMolecule("CCO") # Ethanol backbone
        self.assertEqual(mol.atom_count(), 3)
        self.assertEqual(mol.atoms, ["C", "C", "O"])
        self.assertEqual(mol.bonds, [(0, 1), (1, 2)])

if __name__ == "__main__":
    unittest.main()
