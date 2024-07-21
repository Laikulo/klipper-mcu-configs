from multiprocessing import Array
from pathlib import Path

from .model import McuConfig


class KMCU(object):
    TREE_ROOTS = ['community', 'vendor-official', 'vendor-scraped']

    def build_metadata(self):
        mcu_configs: Array[McuConfig] = []

        for fileset in self.TREE_ROOTS:
            confidence_level = fileset
            tree_dir = Path(self.basedir) / fileset
            if not tree_dir.exists():
                continue
            for vendor_dir in tree_dir.iterdir():
                if not vendor_dir.is_dir():
                    continue
                for product_dir in vendor_dir.iterdir():
                    if not product_dir.is_dir():
                        continue
                    for product_entry in product_dir.iterdir():
                        if product_entry.is_file():
                            mcu_configs.append(McuConfig(
                                provenance=confidence_level,
                                vendor_name=vendor_dir.name,
                                product_name=product_dir.name,
                                variant_name=None,
                                configuration_name=str(product_entry.with_suffix('')),
                                kconfig_file=product_entry,
                                description=None
                            ))
                        elif product_entry.is_dir():
                            mcu_configs += [
                                McuConfig(
                                    provenance=confidence_level,
                                    vendor_name=vendor_dir.name,
                                    product_name=product_dir.name,
                                    variant_name=product_entry.name,
                                    configuration_name=str(variant_entry.with_suffix('')),
                                    kconfig_file=variant_entry,
                                    description=None
                                )
                                for variant_entry in product_entry.iterdir()
                                if variant_entry.is_file()
                            ]
        return mcu_configs

    def __init__(self, basedir: Path):
        self.basedir: Path = basedir


