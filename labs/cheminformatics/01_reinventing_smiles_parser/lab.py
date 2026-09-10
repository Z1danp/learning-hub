"""
Lab 01: Reinventing a Simple Linear Molecule Parser
Domain: Cheminformatics

Problem Challenge:
Kamu ditugaskan membuat parser sederhana yang membaca string atom linier
(seperti 'CCC' untuk Propana atau 'CCN' untuk Etilamina) dan mengembalikan
jumlah atom serta adjacency graph (konektivitas ikatan antar atom).

Format Output:
- atoms: list of atom symbols (e.g. ['C', 'C', 'N'])
- bonds: list of tuple index pairs (e.g. [(0, 1), (1, 2)])
"""

class SimpleMolecule:
    def __init__(self, smiles_str: str):
        self.raw = smiles_str
        self.atoms = []
        self.bonds = []
        self._parse()

    def _parse(self):
        # Logika dasar untuk membaca atom 1 huruf (C, N, O, P, S, F, I)
        if not self.raw:
            return
        
        for i, char in enumerate(self.raw):
            self.atoms.append(char)
            if i > 0:
                self.bonds.append((i - 1, i))

    def atom_count(self) -> int:
        return len(self.atoms)

    def bond_count(self) -> int:
        return len(self.bonds)
