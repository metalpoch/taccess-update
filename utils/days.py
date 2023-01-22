from datetime import datetime, timedelta


def range_days(firstday: str, lastday: str) -> list[str]:
    start = datetime.strptime(firstday, "%Y%m%d")
    end = datetime.strptime(lastday, "%Y%m%d")
    return [
        (start + timedelta(days=d)).strftime("%Y%m%d") for d in range((end - start).days + 1)
    ]
