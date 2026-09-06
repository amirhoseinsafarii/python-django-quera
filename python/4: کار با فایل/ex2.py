def calculate_sums(path: str) -> None:

    with open("result.csv", "w") as f:
        for c in parse_csv(path):
            sum = 0
            for item in range(len(c)):
                sum = int(c[item]) + sum
                print("c[item]:>>>>>>", c[item])
                f.write(c[item].join(" ,"))
            f.write(f" {sum}\n")


def parse_csv(path: str):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.strip().split(",")


calculate_sums(
    "/Users/amirhosseinsafari/projects/python-django-quera/python/4: کار با فایل/ex2File.csv"
)
