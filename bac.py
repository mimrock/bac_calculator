import argparse
import pprint

parser = argparse.ArgumentParser(description='Calculate alcohol.')
parser.add_argument('-weight', type = int, help = 'Weight of the patient in kg')
parser.add_argument('-height', type = int, help = 'Height of the patient in cm')
parser.add_argument('-age', type = int, help = 'Age in years')
parser.add_argument('-female', help = 'Height of the patient in cm', action="store_true")
parser.add_argument('-alc', type = int, help = 'Volume percent of alcohol in the drink')
parser.add_argument('-target', type = float, help = 'Target alcohol concetration in per mille')

args = parser.parse_args()
pprint.pprint(args);
# print(args.accumulate(args.integers))
#calculate body water factor for males by Watson and Watson (1980)
if args.female:
	g = 0.203 - (0.07 * args.age) + (0.1069 * args.height) + (0.2466 * args.weight)
else:
	g = 2.447 - (0.09516 * args.age) + (0.1074 * args.height) + (0.3362 * args.weight)

print ('Body water factor:', g)
#female @todo
# Reduction factor
r = (1.055*g)/(0.8*args.weight)
print ('Reduction factor', r)

#Calculate alcohol to consume in grams
V = args.target * args.weight * r
print ('Alcohol to consume (int grams):', V)

#Calculate drink volume in ml assuming that apart from the alcohol, the drink weights as water
alc_volume = (1/0.789)*V
print ('Volume of the alcohol in ml', alc_volume)

drink_volume = (alc_volume/args.alc)*100
print ('Volume of the drink', drink_volume)

