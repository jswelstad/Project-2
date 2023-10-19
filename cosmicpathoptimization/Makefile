PROGRAM = python3
MAIN = cosmicpathoptimization.py
TESTMAIN = testCosmicPath.py
TEST = pytest
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive
KATTIS = $(PROGRAM) kattis-cli/submit.py

.PHONY: test
test:
	$(TEST) $(TESTMAIN)

.PHONY: run
run:
	$(PROGRAM) $(MAIN)

.PHONY: mypyx	
mypy:
	mypy --strict $(MAIN)
	mypy --strict $(TESTMAIN)

.PHONY: style
style:
	flake8 $(MAIN)
	flake8 $(TESTMAIN)

.PHONY: style-fix
style-fix:
	$(STYLE_FIX) $(MAIN)
	$(STYLE_FIX) $(TESTMAIN)

.PHONY: kattis
kattis:
	$(KATTIS) $(MAIN) 

.PHONY: clean
clean:
	@rm -rf __pycache__
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@echo "All Clean"

.PHONY: all
all: mypy style style-fix clean test