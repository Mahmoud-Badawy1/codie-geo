"""Offline smoke tests using a tiny synthetic upstream archive."""
from pathlib import Path
import io, tempfile, unittest, zipfile, sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import bootstrap

class InstallerTests(unittest.TestCase):
    def test_safe_copy_and_sanitize(self):
        root='geo-seo-claude-main/'
        required=['geo/SKILL.md','skills/geo-audit/SKILL.md','skills/geo-report/SKILL.md','skills/geo-technical/SKILL.md','scripts/fetch_page.py']
        buffer=io.BytesIO()
        with zipfile.ZipFile(buffer,'w') as z:
            for p in required:
                z.writestr(root+p, 'Copyright Zubair Trabzada. Contact admin@example.com\n' if p.endswith('.md') else 'print("unchanged")\n')
            z.writestr(root+'assets/banner.svg','<svg/>')
            z.writestr(root+'skills/geo-audit/images/pic.png','png')
            z.writestr(root+'not-in-scope.txt','hello')
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)
            (base/'vendor').mkdir()
            report=bootstrap.install_from_bytes(buffer.getvalue(),base)
            self.assertEqual(report['file_count'],len(required))
            self.assertEqual((base/'vendor/geo-seo-core/scripts/fetch_page.py').read_text(),'print("unchanged")\n')
            doc=(base/'vendor/geo-seo-core/geo/SKILL.md').read_text()
            self.assertNotIn('Zubair Trabzada',doc)
            self.assertNotIn('admin@example.com',doc)
            self.assertFalse((base/'vendor/geo-seo-core/assets/banner.svg').exists())
            self.assertTrue((base/'vendor/install-manifest.json').exists())
    def test_selected(self):
        self.assertTrue(bootstrap.selected('skills/geo-crawlers/SKILL.md'))
        self.assertFalse(bootstrap.selected('assets/banner.svg'))
        self.assertTrue(bootstrap.selected('scripts/webapp/app.py'))
        self.assertFalse(bootstrap.selected('../bad.md'))
if __name__=='__main__': unittest.main()
