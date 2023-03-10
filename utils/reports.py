import json
from os import path
from sys import exit

import numpy as np
import pandas as pd

from utils import log


def create_json(
    reports: list,
    metadata: dict,
    day: str,
    output: str,
    errors: dict
) -> tuple:

    document = {
        "day": day,
        "reports": []
    }

    report_path = path.join(metadata["path"], day)
    for report in reports:
        filename = path.join(report_path, report)
        names = metadata["columns"]

        try:
            df = pd.read_csv(
                filename,
                header=0,
                names=names,
                sep=metadata["sep"],
                decimal=metadata["decimal"],
            ).fillna(0).replace([np.inf, -np.inf], 0)

        except BaseException as  e:
            type_error = f"CreateJson{e.__class__.__name__}"
            msg_error = e.args[-1].replace("\n", "")
            msg_error = f"{msg_error} on '{report}'"
            if errors.get(type_error):
                errors[type_error].append(msg_error)
            else:
                errors[type_error] = [msg_error]

        else:
            group = report.replace(".csv", "")
            document["reports"].append({
                "group": group,
                "interfaces": df["interfaces"].tolist(),
                "inAvg": df["inAvg"].tolist(),
                "inMax": df["inMax"].tolist(),
                "outAvg": df["outAvg"].tolist(),
                "outMax": df["outMax"].tolist(),
                "bandwidth": df["bandwidth"].tolist(),
                "use": df["use"].tolist(),
            })

    # data without measures
    if len(document["reports"]) == 0:
        type_error = "CreateJsonEmptyReport"
        msg_error = f"data without measures in '{report_path}'"

        if errors.get(type_error):
            errors[type_error].append(msg_error)

        else:
            errors[type_error] = [msg_error]

        return None, errors

    else:
        output_json = path.join(output, f"{day}.json")
        try:
            with open(output_json, "w") as file:
                json.dump(document, file, indent=2)
        except FileNotFoundError:
            print()  # break carriage return
            print(f'The directory "{output}" does not exist')
            exit()
        else:
            return output_json, errors


def create_json_error(output: str, errors: dict) -> None:
    output = path.join(output, "errors.json")
    try:
        with open(output, "w") as file:
            json.dump(errors, file, indent=2)
    except BaseException as e:
        print(f"{e.args[1]} {output}")
        exit()
