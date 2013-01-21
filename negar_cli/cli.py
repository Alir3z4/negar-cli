import sys
import getopt
from negar_cli.helpers import help_message

def main():
    """
    main()
    ======
    """
    output_file = "Negar_Output"
    input_file = ''
    file_name = ''
    # Check if user typed command without any argument,
    # show him how to use negar!
    if len(sys.argv) < 2:
        help_message()
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
        help_message()
        sys.exit(1)
