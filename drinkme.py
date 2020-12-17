#!\usr\bin\env python3
"""
Generate filled-out rubrics for EW401
"""

import argparse
import secrets
import random

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Provide rubrics for EW401")
    parser.add_argument("ofilename",help="output filename")
    args = parser.parse_args()

    rubric_bytes = secrets.token_bytes(36459+random.randint(0,511))
    with open(args.ofilename,'wb') as f:
        f.write(rubric_bytes)
    
        
