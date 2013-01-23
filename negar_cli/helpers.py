from version import __version__

def get_version():
    """
    get_version()
    =============

    Return version number in str

    :rtype: str
    """
    return ".".join(map(str, __version__))

def help_message():
    print("""
Welcome to Negar Persian editor program
Usage: Negar [OPTIONS] -f [INPUT_FILE] -o [OUTPUT-FILE]

Options:
   -h, --help                       Display this help and exit
   -V, --Version                    Print version number and exit
   -f, --file[=INPUT_FILE_NAME]     Specify [INPUT_FILE]. The file who you want to edit
   -o, --output[=OUTPUT_FILE_NAME]  Specify [OUT_PUT_FILE]. The file who you want the programs
                                    output writes into it. If you don't specify this option
                                    Negar will generate an auto file to save the result.
       --gui                        Run negars graphical user interface (GUI)
       --fix-dashes                 Disable fix dashes feature
       --fix-three-dots             Disable fix three dots feature
       --fix-english-quotes         Disable fix english quotes feature
       --fix-hamzeh                 Disable fix 'Hamzeh' feature
       --hamzeh-with-yeh            Use 'Hamzeh' instead of 'yeh' for fix 'Hamzeh' feature
       --fix-spacing-bq             Disable fix spacing braces and 'qoutes' feature
       --fix-arabic-num             Disable fix arabic num feature
       --fix-english-num            Disable fix english num feature
       --fix-non-persian-chars      Disable fix misc non persian chars feature
       --fix-p-spacing              Disable fix prefix spacing feature
       --fix-p-separate             Disable fix prefix separating feature
       --fix-s-spacing              Disable fix suffix spacing feature
       --fix-s-separate             Disable fix suffix separating feature
       --aggresive                  Disable aggresive feature
       --cleanup-kashidas           Disable cleanup 'kashidas' feature
       --cleanup-ex-marks           Disable cleanup extra marks feature
       --cleanup-spacing            Disable cleanup spacing feature


Version:
Negar: {negar_version}
Negar-CLI: {cli_version}

Exit status:
0   if OK,
1   if unknown argument passed to the Negar.

To get more information visit the website: http://github.com/OpenSourceMotherFucker/negar-cli
        """.format(
        negar_version='0.6.1',
        cli_version=get_version()
    ))
