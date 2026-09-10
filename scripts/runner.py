"""
Agentic Learning Hub CLI Runner
Usage:
  py scripts/runner.py test <path_to_test_file>
  py scripts/runner.py new-note <domain> "<title>"
  py scripts/runner.py new-lab <domain> "<lab_name>"
"""

import sys
import os
import subprocess
from pathlib import Path
from datetime import date

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent

def run_test(test_path: str):
    p = Path(test_path)
    if not p.is_absolute():
        p = ROOT_DIR / p

    if not p.exists():
        print(f"[ERROR] File test tidak ditemukan: {p}")
        sys.exit(1)

    print(f"[TEST] Menjalankan test: {p}")
    if p.suffix == ".py":
        test_dir = str(p.parent)
        env = os.environ.copy()
        env["PYTHONPATH"] = test_dir + os.pathsep + env.get("PYTHONPATH", "")
        res = subprocess.run([sys.executable, "-m", "unittest", p.name], cwd=test_dir, env=env)
        sys.exit(res.returncode)
    elif p.suffix in (".ts", ".js"):
        res = subprocess.run(["node", "--test", str(p)], shell=True, cwd=str(p.parent))
        sys.exit(res.returncode)
    else:
        print(f"[ERROR] Tipe file tidak didukung: {p.suffix}")
        sys.exit(1)

def create_note(domain: str, title: str):
    valid_domains = ["cheminformatics", "webdev", "hybrid_apps"]
    if domain not in valid_domains:
        print(f"[ERROR] Domain harus salah satu dari: {valid_domains}")
        sys.exit(1)

    slug = title.lower().replace(" ", "-").replace("/", "-")
    note_dir = ROOT_DIR / "notes" / domain
    note_dir.mkdir(parents=True, exist_ok=True)
    note_path = note_dir / f"{slug}.md"

    if note_path.exists():
        print(f"[WARN] Catatan sudah ada: {note_path}")
        return

    template_path = ROOT_DIR / "templates" / "note_template.md"
    template = template_path.read_text(encoding="utf-8")
    content = template.replace("{{TITLE}}", title).replace("{{DOMAIN}}", domain).replace("{{DATE}}", str(date.today()))
    note_path.write_text(content, encoding="utf-8")
    print(f"[SUCCESS] Catatan baru berhasil dibuat: {note_path}")

def create_lab(domain: str, lab_name: str):
    valid_domains = ["cheminformatics", "webdev", "fullstack_chem_apps"]
    if domain not in valid_domains:
        print(f"[ERROR] Domain harus salah satu dari: {valid_domains}")
        sys.exit(1)

    slug = lab_name.lower().replace(" ", "_")
    lab_dir = ROOT_DIR / "labs" / domain / slug
    lab_dir.mkdir(parents=True, exist_ok=True)

    if domain == "cheminformatics":
        lab_file = lab_dir / "lab.py"
        test_file = lab_dir / "test_lab.py"
        tmpl = (ROOT_DIR / "templates" / "chem_lab_template.py").read_text(encoding="utf-8")
        lab_file.write_text(tmpl.replace("{{TOPIC}}", lab_name).replace("{{PROBLEM_DESCRIPTION}}", "Jelaskan masalah lab di sini."), encoding="utf-8")
        test_file.write_text("""import unittest
from lab import solve_challenge

class TestLab(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
""", encoding="utf-8")
    else:
        lab_file = lab_dir / "lab.ts"
        test_file = lab_dir / "lab.test.ts"
        tmpl = (ROOT_DIR / "templates" / "web_lab_template.ts").read_text(encoding="utf-8")
        lab_file.write_text(tmpl.replace("{{TOPIC}}", lab_name).replace("{{PROBLEM_DESCRIPTION}}", "Jelaskan masalah lab di sini."), encoding="utf-8")
        test_file.write_text("""import { test } from 'node:test';
import assert from 'node:assert';
import { solveChallenge } from './lab.ts';

test('starter test', () => {
  assert.strictEqual(typeof solveChallenge, 'function');
});
""", encoding="utf-8")

    print(f"[SUCCESS] Lab baru berhasil disiapkan di: {lab_dir}")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "test" and len(sys.argv) >= 3:
        run_test(sys.argv[2])
    elif cmd == "new-note" and len(sys.argv) >= 4:
        create_note(sys.argv[2], sys.argv[3])
    elif cmd == "new-lab" and len(sys.argv) >= 4:
        create_lab(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
