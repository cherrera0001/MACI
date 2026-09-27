"""Regresiones: plantilla truncada y conceptos confundidos con exámenes."""
import unittest
from pathlib import Path

from datito_loop_eval import gates, profundidad_certamen

GOOD = '''<!doctype html><html><head><!-- datito:template:v1 -->
<title>Generalización</title><style>:root{--tinta:#1a1a1a;--morado:#7c3aed}</style>
</head><body><main><h1>Generalización</h1><p>Lee el certamen y su subpregunta.</p>
</main></body></html>'''


class LecturaRegressionTests(unittest.TestCase):
    def test_concept_is_not_exam_due_to_navigation(self):
        self.assertEqual({}, profundidad_certamen(GOOD, Path('07_generalizacion.html')))

    def test_real_exam_still_requires_depth(self):
        result = profundidad_certamen(GOOD, Path('certamen_3.html'))
        self.assertEqual(4, len(result))
        self.assertFalse(any(result.values()))

    def test_exam_heading_is_detected_without_filename(self):
        html = GOOD.replace('<h1>Generalización', '<h1>Certamen 3')
        self.assertIn('details_resp', profundidad_certamen(html))

    def test_rule_comment_cannot_satisfy_exam_depth(self):
        html = GOOD + '<!-- Qué pasó, Cómo se resuelve, error típico -->'
        result = profundidad_certamen(html, Path('certamen_3.html'))
        self.assertFalse(any(result.values()))

    def test_good_structure_then_truncated_head(self):
        self.assertTrue(all(gates(GOOD).values()))
        broken = GOOD.replace('<title>', '<!-- reglas truncadas <title>')
        broken = broken.replace('<main>', '<main><!-- datito:nav:inicio -->')
        self.assertFalse(gates(broken)['document_structure'])
        self.assertFalse(gates(broken)['canonical_root'])

    def test_duplicate_template_tail_is_rejected(self):
        broken = GOOD.replace('</main>', '<h1>TÍTULO DEL CONCEPTO</h1></main>')
        self.assertFalse(gates(broken)['document_structure'])
        self.assertFalse(gates(broken)['no_template_placeholders'])

    def test_duplicate_or_alternate_root_is_rejected(self):
        self.assertFalse(gates(GOOD.replace('</style>', ':root{--x:1}</style>'))['canonical_root'])
        self.assertFalse(gates(GOOD.replace('#1a1a1a', '#1c1f24'))['canonical_root'])


if __name__ == '__main__':
    unittest.main()
