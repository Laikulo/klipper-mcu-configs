import logging
from pathlib import Path

class KMCU(object):
    TREE_ROOTS = ['community', 'vendor-official', 'vendor-scraped']
    def build_metadata(self):
        meta_tree = {}

        for fileset in self.TREE_ROOTS;

        pass

    def __init__(self, basedir: Path):
        self.basedir: Path = basedir


