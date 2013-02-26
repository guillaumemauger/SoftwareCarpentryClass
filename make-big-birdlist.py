
# triple quoting allows multiple lines to go in one quote
birdnames = """\
Common Teal
Long-tailed Duck
Little Grebe
Albatross
Flamingo
Heron
Stork
Shoebill
Vulture
Bald Eagle""".splitlines()

states = """Kentucky
Missouri
Kansas
Maine
Michigan
New York""".splitlines()

# define function to get random date:
import random, datetime
def generate_random_day(year):
    doy = int(random.gauss(200, 50))
    doy = min(doy, 365)
    doy = max(doy, 1)
    datestr = "%s %s" % (doy, year)
    date = datetime.datetime.strptime(datestr, "%j %Y")
    new_date = date.strftime("%B %d")
    return new_date.lower()

# define function to generate random obsevation:
def generate_random_observation():
    bird = random.choice(birdnames).lower()
    state = random.choice(states).lower()
    day = generate_random_day(2013)
    return bird, state, day # shorthand for outputting a tuple

# write file of random obs:
import csv
fp = file('long-birds.csv', 'wb')
w = csv.writer(fp) # write a csv ... could change to space delimited using delimiter=" "

for i in range(10000):
    row = generate_random_observation()
    w.writerow(row)
fp.close() # important esp for writing files ("needs to be flushed to disk")




