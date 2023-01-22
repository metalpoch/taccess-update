def __days_counter(n: int) -> str:
    return f"{n} day processed" if n == 1 else f"{n} days processed"


def __errors_counter(e: dict) -> str:
    n_warn, n_err = 0, 0

    for k in e.keys():
        if k == "FileNotFoundError":  # msg_error
            n_err += len(e[k])
        else:  # other erros as msg_warning
            n_warn += len(e[k])

    if n_err == 1:
        msg = f"{n_err} day error"
        msg_error = f"-\x1b[1;31m {msg} \x1b[0;0m"
    elif n_err > 1:
        msg = f"{n_err} day errors"
        msg_error = f"-\x1b[1;31m {msg} \x1b[0;0m"
    else:
        msg_error = ""

    if n_warn == 1:
        msg = f"{n_warn} error read csv"
        msg_warning = f"-\x1b[1;31m {msg} \x1b[0;0m"
    elif n_warn > 1:
        msg = f"{n_warn} errors read csv"
        msg_warning = f"-\x1b[1;33m {msg} \x1b[0;0m"
    else:
        msg_warning = ""


    return msg_warning + msg_error


def __updates(n: int) -> str:
    if n == 0:
        return ""
    elif n > 1:
        msg = f"{n} updates"
    else:
        msg = f"{n} update"
    return(f"-\x1b[1;32m {msg} \x1b[0;0m")


def error(text: str) -> None:
    print("\x1b[1;31m" + text + "\x1b[0;0m")


def percentage(current: int, limit: int, errors: dict, updates: int) -> None:
    percent = round(current * 100 / limit, 2)
    n_days = __days_counter(current)
    n_errors = __errors_counter(errors)
    n_updates = __updates(updates)

    print(f"\r{percent}% -> {n_days} {n_errors} {n_updates}", end="")



