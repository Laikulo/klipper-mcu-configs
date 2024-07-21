.PHONEY: metadata

metadata: output/kconfigs.json

output/kconfigs.json: wheel-installed.flag
	kmcu_metadata

wheel-installed.flag: dist/kmcu_tools-0.0.0-py3-none-any.whl
	pip install --no-deps --force-reinstall dist/kmcu_tools-0.0.0-py3-none-any.whl
	touch wheel-installed.flag

dist/kmcu_tools-0.0.0-py3-none-any.whl:
	pyproject-build
