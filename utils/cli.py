import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--update",
    type=str,
    required=False,
    default=False,
    help="Update taccess with the endpoint"
)
parser.add_argument(
    "--layer",
    dest="layer",
    type=str,
    required=True,
    help="Layer of reports to process"
)
parser.add_argument(
    "--firstday",
    type=str,
    required=True,
    help="First day to obtain the data (formated as '%%Y%%m%%d')"
)
parser.add_argument(
    "--lastday",
    type=str,
    required=True,
    help="Last day to obtain the data (formated as '%%Y%%m%%d')"
)
parser.add_argument(
    "--output",
    type=str,
    required=True,
    help="Output directory of files"
)

args = parser.parse_args()


