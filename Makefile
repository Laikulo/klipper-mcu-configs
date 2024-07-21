.PHONEY: metadata

metadata: output/kconfigs.json

output/kconfigs.json: venv/bin/kmcu_metadata
	./venv/bin/kmcu_metadata

venv/bin/kmcu_metadata: dist/kmcu_tools-0.0.0-py3-none-any.whl
	pip install --no-deps --force-reinstall dist/kmcu_tools-0.0.0-py3-none-any.whl
dist/kmcu_tools-0.0.0-py3-none-any.whl:
	pyproject-build
