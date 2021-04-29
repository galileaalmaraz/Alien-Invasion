import csv


class GameScore:
    CSV_FILENAME = "./scores.csv"
    FIELDNAMES = ["username", "duration", "score"]

    def __init__(self, username, duration, score):
        self.username = username
        self.duration = duration
        self.score = score

    def _get_self_dict(self):
        return {field: getattr(self, field) for field in self.FIELDNAMES}

    def _does_header_exist(self):
        header_exists = False
        with open(self.CSV_FILENAME, "r") as f:
            if f.readline().strip().split(",") == self.FIELDNAMES:
                header_exists = True
        return header_exists

    def save(self):
        with open(self.CSV_FILENAME, "a") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            if not self._does_header_exist():
                writer.writeheader()
            writer.writerow(self._get_self_dict())


def main():
    score = GameScore("Mena", 312, 312313)
    score.save()


if __name__ == "__main__":
    main()
