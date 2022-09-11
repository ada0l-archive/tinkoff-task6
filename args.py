import sys


def parse_args_from_sys():
    result = dict()

    for item in sys.argv[1:]:
        arg, value = item.split("=")
        arg = arg.replace("--", "")
        result[arg] = value

    return result


def prepare_args(args_promt):
    args = parse_args_from_sys()

    for arg_name, arg_promt in zip(args_promt.keys(), args_promt.values()):
        if arg_name not in args and arg_promt is not None:
            args[arg_name] = input(arg_promt)
        if arg_name not in args and arg_promt is None:
            args[arg_name] = None

    return args
