#!/usr/bin/python
'''
negar-cli

Usage:
    negar-cli -h
    negar-cli -i <INPUTFILE> [-o <OUTPUTFILE>]
    negar-cli -i <INPUTFILE> [--aggresive --cleanup-ex-marks --cleanup-kashidas --cleanup-sapcing --fix-arabic-num --fix-dashes --fix-english-num --fix-english-quotes --fix-hamzeh --fix-non-persian-chars --fix-p-separate --fix-p-spacing --fix-s-separate --fix-s-spacing --fix-spacing-bq fix-three-dots --hamzeh-with-yeh -o <OUTPUTFILE>]

options:
    -h, --help                   print help message.
    -i FILE, --input-file=FILE   declare input file.
    -o FILE, --output-file=FILE  declare output file.-h [default: negar_output]
    --aggresive                  Disable aggresive feature 
    --cleanup-ex-marks           Disable cleanup extra marks feature 
    --cleanup-kashidas           Disable cleanup kashidas feature 
    --cleanup-spacing            Disable cleanup spacing feature 
    --fix-arabic-num             Disable fix arabic num feature 
    --fix-dashes                 Disable fix dashes feature 
    --fix-english-num            Disable fix english num feature
    --fix-english-quotes         Disable fix english quotes feature
    --fix-hamzeh                 Disable fix hamzeh feature  
    --fix-non-persian-chars      Disable fix misc non persian chars feature
    --fix-p-separate             Disable fix perfix separating feature 
    --fix-p-spacing              Disable fix perfix spacing feature 
    --fix-s-separate             Disable fix suffix separating feature 
    --fix-s-spacing              Disable fix suffix spacing feature 
    --fix-spacing-bq             Disable fix spacing braces and qoutes feature
    --fix-three-dots             Disable fix three dots feature  
    --hamzeh-with-yeh            Use 'Hamzeh' instead of 'yeh' for fix hamzeh feature 

'''
import sys
from docopt import docopt
from negar import virastar

def main(args):
    """
    main()
    ======
    """
    output_file = args['--output-file']
    file_name = args['--input-file']
    argli=[]
    if args['--aggresive']: argli.append('aggresive')
    if args['--cleanup-ex-marks']: argli.append('cleanup-ex-marks')
    if args['--cleanup-kashidas']: argli.append('cleanup-kashidas')
    if args['--cleanup-spacing']: argli.append('cleanup-spacing')
    if args['--fix-arabic-num']: argli.append('fix-arabic-num')
    if args['--fix-dashes']: argli.append('fix-dashes')
    if args['--fix-english-num']: argli.append('fix-english-num')
    if args['--fix-english-quotes']: argli.append('fix-english-quote')
    if args['--fix-hamzeh']: argli.append('fix-hamzeh')
    if args['--fix-non-persian-chars']: argli.append('fix-non-persian-chars')
    if args['--fix-p-separate']: argli.append('fix-p-separate')
    if args['--fix-p-spacing']: argli.append('fix-p-spacing')
    if args['--fix-s-separate']: argli.append('fix-s-separate')
    if args['--fix-s-spacing']: argli.append('fix-s-spacing')
    if args['--fix-spacing-bq']: argli.append('fix-spacing-bq')
    if args['--fix-three-dots']: argli.append('fix-three-dots')
    if args['--hamzeh-with-yeh']: argli.append('hamzeh-with-yeh')

    try:
        input_file = open(file_name)
        output_file = open(output_file, 'w')
        while True:
            line = unicode(input_file.readline(), encoding='utf-8')
            if len(line) == 0:
                break
            run_PE = virastar.PersianEditor(line, *argli)
            output_file.write(run_PE.cleanup().encode('utf-8'))
            
    except:
        print("boos")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print __doc__
        exit()

    main(docopt(__doc__))
