#!/bin/sh

python make-big-birdlist.py

grep michigan long-birds.csv | grep ctober | sort -k1 -t, > sort_michigan_october_birds

python make-big-birdlist.py

cat sort_michigan_october_birds >> long-birds.csv

