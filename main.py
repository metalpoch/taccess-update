import json
import re
from os import listdir, path
from sys import exit

from utils import cli, log, taccess_update
from utils.days import range_days
from utils.reports import create_json, create_json_error

PATH = path.dirname(path.abspath(__file__))
with open(path.join(PATH, "config.json"), "r") as file:
    CONFIG = json.load(file)


def setting_layer() -> dict[str, str]:
    layer = cli.args.layer
    settings = CONFIG["LAYERS"]
    settings = settings[layer] if settings.get(layer) else False

    if not settings:
        print(f"The layer {layer} is invalid")
        exit()

    else:
        return {
            "layer": layer,
            "path": settings["path"],
            "columns": settings["columns"],
            "sep": settings["sep"],
            "decimal": settings["decimal"],
            "blacklist": CONFIG["BLACKLIST"]
        }


def url_endpoint(endpoint: str) -> tuple:
    endpoints = CONFIG["API_ENDPOINTS"]
    access_token = CONFIG["API_ACCESS_TOKEN"]
    if endpoints.get(endpoint):
        return endpoints[endpoint], access_token
    else:
        print(f"The endpoint {endpoint} is invalid")
        exit()


def main() -> None:
    count = 1
    updates = 0
    errors = {}
    output = cli.args.output
    endpoint = cli.args.update

    metadata = setting_layer()
    if endpoint:
        url, access_token = url_endpoint(endpoint)

    days = range_days(cli.args.firstday, cli.args.lastday)
    lenght = len(days)

    for day in days:
        reports_dir = path.join(metadata["path"], day)
        blacklist = metadata["blacklist"]

        try:
            files = listdir(reports_dir)

        except BaseException as e:
            type_error = e.__class__.__name__
            msg_error = f"{e.args[-1]} {reports_dir}"
            if errors.get(type_error):
                errors[type_error].append(msg_error)
            else:
                errors[type_error] = [msg_error]

        else:
            blacklist = re.compile("|".join(blacklist))
            reports = list(
                filter(lambda x: not re.search(blacklist, x.lower()), files)
            )
            output_json, errors = create_json(
                day=day,
                reports=reports,
                metadata=metadata,
                output=output,
                errors=errors
            )

            if endpoint:
                update_success, errors = taccess_update.post(
                    url=url,
                    access_token=access_token,
                    file=output_json,
                    errors=errors
                )
                updates += 1 if update_success else 0

        log.percentage(
            current=count,
            limit=lenght,
            errors=errors,
            updates=updates
        )
        count += 1

    print()
    if len(errors):
        create_json_error(output=output, errors=errors)


if __name__ == "__main__":
    main()
