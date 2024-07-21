import dataclasses
from pathlib import Path
from typing import Optional


@dataclasses.dataclass
class McuConfig:
    provenance: str
    vendor_name: str
    product_name: str
    variant_name: Optional[str]
    configuration_name: str
    kconfig_file: Path
    description: Optional[str]

    def to_dict(self):
        return {
            "vendor": self.vendor_name,
            "product": self.product_name,
            "variant": self.variant_name,
            "configuration": self.configuration_name,
            "description": self.description,
            "provenance": self.provenance,
            "kconfig_path": str(self.kconfig_file)
        }
