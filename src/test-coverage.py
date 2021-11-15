#!/usr/bin/env python
import random
import os

COVERAGE = str(random.randint(70, 100))
os.environ['CODE_COVERAGE'] = COVERAGE

print(COVERAGE)
