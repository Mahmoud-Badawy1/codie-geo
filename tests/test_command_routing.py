import json
from pathlib import Path
import importlib.util
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('router',ROOT/'codie_geo.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
EXPECTED='audit quick citability crawlers llmstxt brands platforms schema technical content-audit report report-pdf'.split()
class TestRouting(unittest.TestCase):
    def test_default_is_all(self):
        self.assertEqual(mod.route([])['command'],'all')
        self.assertEqual(mod.route(['/codie-geo'])['command'],'all')
        self.assertEqual(mod.route(['/codie-geo','https://example.com'])['command'],'all')
    def test_specialists(self):
        reg=json.loads((ROOT/'commands.json').read_text())
        for command in EXPECTED:
            self.assertIn(command,reg['audit_commands'])
            path=mod.route(['/codie-geo',command,'https://example.com'])['path']
            self.assertTrue(path.endswith('/SKILL.md'),path)
    def test_content_disambiguation(self):
        self.assertEqual(mod.route(['/codie-geo','content','https://example.org'])['path'],'skills/codie-geo-content-audit/SKILL.md')
        self.assertEqual(mod.route(['/codie-geo','content'])['path'],'skills/codie-geo-create/SKILL.md')
    def test_local_paths(self):
        reg=json.loads((ROOT/'commands.json').read_text())
        for c,p in reg['workflow_commands'].items():
            self.assertTrue((ROOT/p).exists(),f'{c}: {p}')
    def test_one_namespace(self):
        s=(ROOT/'SKILL.md').read_text()
        self.assertIn('`/codie-geo` **means RUN THE FULL PIPELINE**',s)
        self.assertIn('content-audit',s)
        self.assertTrue((ROOT/'vendor/UPSTREAM_LICENSE.txt').exists())
if __name__=='__main__':unittest.main()
