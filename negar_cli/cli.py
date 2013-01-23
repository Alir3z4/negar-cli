import sys
import getopt
from negar.virastar import PersianEditor
import helpers

#TODO: This is bullshit, Should be handled by `negar` itself.
negar_version = '0.6.1'

def main():
    """
    main()
    ======
    """
    output_file = "negar_output"
    input_file = ''
    file_name = ''
    # Check if user typed command without any argument,
    # show him how to use negar!
    if len(sys.argv) < 2:
        helpers.help_message()
        exit(0)
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "hVgf:o:",
            ["help","file=","output=", "Version", "gui", "fix-dashes",
             "fix-three-dots", "fix-english-quotes", "fix-hamzeh",
             "hamzeh-with-yeh", "fix-spacing-bq", "fix-arabic-num",
             "fix-english-num", "fix-non-persian-chars", "fix-p-spacing",
             "fix-p-separate", "fix-s-spacing", "fix-s-separate", "aggresive",
             "cleanup-kashidas", "cleanup-ex-marks", "cleanup-spacing",
             "add-untouch-list="]
        )
    except getopt.GetoptError, err:
        print(err)
        helpers.help_message()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ['-h', '--help']:
            helpers.help_message()
            sys.exit(0)
        elif opt in ['-V', '--Version']:
            print("You are using Negar version: %s" % negar_version)
        elif opt in '--fix-non-persian-chars':
            args.append('fix-non-persian-chars')
        elif opt in ['-f', '--file']: file_name = arg
        elif opt in ['-o', '--output']: output_file = arg
        elif opt in '--fix-dashes':  args.append('fix-dashes')
        elif opt in '--fix-three-dots':  args.append('fix-three-dots')
        elif opt in '--fix-english-quotes': args.append('fix-english-quotes')
        elif opt in '--fix-hamzeh': args.append('fix-hamzeh')
        elif opt in '--hamzeh-with-yeh': args.append('hamzeh-with-yeh')
        elif opt in '--fix-spacing-bq': args.append('fix-spacing-bq')
        elif opt in '--fix-arabic-num': args.append('fix-arabic-num')
        elif opt in '--fix-english-num': args.append('fix-english-num')
        elif opt in '--fix-p-spacing': args.append('fix-p-spacing')
        elif opt in '--fix-p-separate': args.append('fix-p-separate')
        elif opt in '--fix-s-separate': args.append('fix-s-separate')
        elif opt in '--aggresive': args.append('aggresive')
        elif opt in '--cleanup-kashidas': args.append('cleanup-kashidas')
        elif opt in '--cleanup-ex-marks': args.append('cleanup-ex-marks')
        elif opt in '--cleanup-spacing': args.append('cleanup-spacing')

    try:
        input_file = open(file_name)
        output_file = open(output_file, 'w')
        while True:
            line = unicode(input_file.readline(), encoding='utf-8')
            if len(line) == 0:
                break
            pe_editor = PersianEditor(line, *args)
            output_file.write(pe_editor.cleanup().encode('utf-8'))
    finally:
        input_file.close()


if __name__ == "__main__":
    main()
