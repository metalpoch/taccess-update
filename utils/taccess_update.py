import json
import requests


def post(url: str, access_token: str, file: str, errors: dict) -> tuple:
    with open(file, 'r') as f:
        data = json.load(f)

    success = False
    headers = {"Authorization": f"access_token {access_token}"}

    try:
        r = requests.post(url=url, json=data, headers=headers)

    except requests.exceptions.Timeout:
        type_error = "UpdateTimeout"
        msg_error = f"refused connection with '{url}'"
        if errors.get(type_error):
            errors[type_error].append(msg_error)
        else:
            errors[type_error] = [msg_error]

    except requests.exceptions.HTTPError:
        type_error = "UpdateHTTPError"
        msg_error = f"failed regular or rare invalid HTTP response on '{url}'"
        if errors.get(type_error):
            errors[type_error].append(msg_error)
        else:
            errors[type_error] = [msg_error]

    except requests.exceptions.ConnectionError:
        type_error = "UpdateConnectionError"
        msg_error = f"request times out on '{url}'"
        if errors.get(type_error):
            errors[type_error].append(msg_error)
        else:
            errors[type_error] = [msg_error]

    else:
        status_code = r.status_code

        if status_code != 200:
            type_error = "UpdateStatuCode"
            msg_error = f"Status {status_code} responsed from '{url}' on {file}"
            if errors.get(type_error):
                errors[type_error].append(msg_error)
            else:
                errors[type_error] = [msg_error]
        else:
            success = True
    return success, errors
