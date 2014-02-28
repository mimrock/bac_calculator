bac_calculator
==============

Blood Alcohol Content Calculator. Based on: Widmark M. P. (1932), Watson P.E. (1989)

usage: bac.py [-h] [-weight WEIGHT] [-height HEIGHT] [-age AGE] [-female]
              [-alc ALC] [-target TARGET]
              
Example:
$ python3 bac.py -weight 82 -height 189 -age 29 -alc 38 -target 0.6
Namespace(age=29, alc=38, female=False, height=189, target=0.6, weight=82)
Body water factor: 47.55436
Reduction factor 0.7647842957317073
Alcohol to consume (int grams): 37.62738734999999
Volume of the alcohol in ml 47.68997129277565
Volume of the drink 125.49992445467278

Which means a 29 years old guy with a weight of 82 kg, and a height of 189 cm needs to drink 125 ml of 38% vodka to reach 0.6 permille (0.06 %) BAC level.

Note that the script does not calculate with the disposal of the alcohol in the body, neither some of the factors that affects the absorption, like the content of the stomach.
