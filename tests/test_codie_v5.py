from pathlib import Path
import json
import importlib.util
import unittest

ROOT=Path(__file__).resolve().parents[1]

class TestCodieV5Package(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg=json.loads((ROOT/'commands.json').read_text(encoding='utf8'))
        spec=importlib.util.spec_from_file_location('codie_geo_v5',ROOT/'codie_geo.py')
        cls.agent=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.agent)

    def test_every_command_has_installed_local_file(self):
        for cmd in [*self.reg['audit_commands'],*self.reg['workflow_commands']]:
            with self.subTest(cmd=cmd):
                resolved=self.agent.route(['/codie-geo',cmd,'https://example.org'])
                self.assertTrue(resolved['installed'],resolved)
                self.assertTrue((ROOT/resolved['path']).exists())

    def test_default_is_complete_workflow(self):
        for args in [[], ['/codie-geo'], ['/codie-geo','https://example.org'], ['/codie-geo','all']]:
            with self.subTest(args=args):
                obj=self.agent.route(args)
                self.assertEqual(obj['path'],'skills/codie-geo-all/SKILL.md')

    def test_content_vs_content_audit(self):
        self.assertEqual(self.agent.route(['/codie-geo','content'])['path'],'skills/codie-geo-create/SKILL.md')
        self.assertEqual(self.agent.route(['/codie-geo','content','https://example.org'])['path'],'skills/codie-geo-content-audit/SKILL.md')
        self.assertEqual(self.agent.route(['/codie-geo','create'])['path'],'skills/codie-geo-create/SKILL.md')

    def test_all_skill_folder_names_and_frontmatter(self):
        skills=sorted((ROOT/'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills),32)
        for skill in skills:
            with self.subTest(skill=str(skill)):
                self.assertTrue(skill.parent.name.startswith('codie-geo-'))
                self.assertIn('name: '+skill.parent.name+'\n',skill.read_text(encoding='utf8'))

    def test_agent_names_and_required_guide_files(self):
        agents=list((ROOT/'agents').glob('*.md'))
        self.assertEqual(len(agents),5)
        self.assertTrue(all(p.name.startswith('codie-geo-') for p in agents))
        for f in ['README.md','QUICKSTART.md','EDITORIAL_PLAYBOOK.md','COMMANDS.md','orchestrator/SKILL.md',
                  'workflows/onboarding.md','workflows/research.md','workflows/content.md',
                  'workflows/social.md','workflows/qa.md','workflows/storage.md',
                  'editorial/copywriting.md','editorial/source-prompt-adaptation.md','editorial/visual-search.md']:
            self.assertTrue((ROOT/f).is_file(),f)

    def test_platforms_and_public_commands(self):
        for name in ['instagram','linkedin','x','reddit','facebook']:
            self.assertTrue((ROOT/f'skills/codie-geo-{name}/SKILL.md').exists())
            self.assertTrue((ROOT/f'platforms/{name}.md').exists())
        readme=(ROOT/'README.md').read_text(encoding='utf8')
        for command in ['audit','quick','citability','crawlers','llmstxt','brands','platforms','schema',
                        'technical','content-audit','report','report-pdf','plan','research','create','social','qa']:
            self.assertIn('/codie-geo '+command,readme)
        for heading in ['full website audit','GEO scoring breakdown','Easy setup']:
            self.assertIn(heading.lower(),readme.lower())

    def test_optional_vendor_is_not_claimed_installed(self):
        info=self.agent.route(['/codie-geo','audit','https://example.org'])
        self.assertTrue(info['installed'])
        self.assertFalse(info['upstream_available'])
        self.assertIn('vendor/geo-seo-core/skills/geo-audit',info['optional_upstream_path'])

if __name__=='__main__': unittest.main()
