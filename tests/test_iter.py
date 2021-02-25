from __future__ import unicode_literals

from cmarkgfm import cmark
from cmarkgfm import _cmark

def test_iter():
    text = u"Hello, **world**!"
    node = cmark.parse_document(text)
    events = [
        evt for evt,node in cmark.iter_document(node)
    ]
    assert events == [2, 2, 2, 2, 2, 3, 2, 3, 3]
