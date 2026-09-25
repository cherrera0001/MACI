#!/usr/bin/env python
"""MACI Platform CLI — unified entry point.

Usage:
    python platform.py status      # Show capability matrix
    python platform.py report      # Generate capability report
    python platform.py process --course 80014  # Process a course
"""

import sys
import os

# Add 03_CODIGO to path so we can import maci_platform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '03_CODIGO'))

from maci_platform.cli import main

if __name__ == '__main__':
    sys.exit(main())
