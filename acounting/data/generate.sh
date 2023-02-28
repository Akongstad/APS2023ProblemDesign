#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution accepted.py              

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2

tc  random1 generate_random 
tc  random2 generate_random
tc  random3 generate_random
tc  random4 generate_random
tc  random5 generate_random
tc  edge1 generate_explicit 0 0 0
tc  edge2 generate_explicit -1 0 1 