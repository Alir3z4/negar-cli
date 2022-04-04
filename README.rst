=========
Negar CLI
=========
Negar Command Line Interface


How to use
==========

Usage of `negar-cli`:

    $ negar-cli [ARGUMENTS] -f [INPUT_FILENAME] -o [OUTPUT_FILENAME]

Arguments are:

    -h, --help                       Display this help and exit
    -V, --Version                    Print version number and exit
    -i, --input-file=INPUT_FILE_NAME    Specify [INPUT_FILE]. The file who you want to edit
    -o, --output-file=OUTPUT_FILE_NAME  Specify [OUT_PUT_FILE]. The file who you want the programs
                                     output writes into it. If you don't specify this option
                                     Negar will generate an auto file to save the result.
    --gui                        Run negar's graphical user interface (GUI)
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
    --trim-lt-whitespaces        Disable trim leading trailing whitespaces

