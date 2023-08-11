are_all_package_installed() {
	python -c "import sys, pkg_resources; sys.exit(0 if all(pkg_resources.require(line.strip()) for line in open('requirements.txt')) else 1)"
}

[ ! -d venv ] && python -m venv venv || echo "DEBUG Found venv"
source venv/bin/activate
[ -f requirements.txt ] && {
	 are_all_package_installed && echo "DEBUG All packages in requirements.txt are installed." || {
		echo "DEBUG pip install -r requirements.txt"
		pip install -r requirements.txt
	 }
} || echo "No requirements.txt"
