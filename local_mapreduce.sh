#!/bin/bash

echo "foo foo quux labs foo bar quux" | ./mapper.py | sort -k1,1 | ./reducer.py
