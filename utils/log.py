def __days_counter(n: int) -> str:
    return f"{n} day processed" if n == 1 else f"{n} days processed"


def __errors_counter(e: dict) -> str:
    n_csv, n_core, n_update = 0, 0 ,0
    for k in e:
        if k.startswith("CreateJson"):
            n_csv = len(e[k])
        elif k.startswith("Update"):
            n_update = len(e[k])
        else:
            n_core = len(e[k])

    msg_csv = f"-\x1b[1;36m {n_csv} csv errors \x1b[0;0m"
    msg_core = f"-\x1b[1;31m {n_core} core errors \x1b[0;0m"
    msg_update = f"-\x1b[1;33m {n_update} update errors \x1b[0;0m"

    return msg_csv + msg_update + msg_core


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

    print(f"\r{percent}% -> {n_days} {n_updates} {n_errors}", end="")



