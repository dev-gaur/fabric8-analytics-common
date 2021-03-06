"""Module with class that handle smoke test results."""
import csv


class SmokeTests:
    """Class that handle smoke test results."""

    INPUT_FILES = {
        "production": {
            "logs": "smoketests_prod.log",
            "results": "smoketests_prod.results"
        },
        "stage": {
            "logs": "smoketests_stage.log",
            "results": "smoketests_stage.results"
        }
    }

    def __init__(self):
        """Construct an instance of the class."""
        self._results = {}
        self._logs = {}

    def read_logs(self):
        """Read logs for all systems (stage, production)."""
        for system, filenames in SmokeTests.INPUT_FILES.items():
            input_file = filenames["logs"]
            with open(input_file) as fin:
                self._logs[system] = fin.read()

    def read_results(self):
        """Read results generated by all smoke tests."""
        for system, filenames in SmokeTests.INPUT_FILES.items():
            input_file = filenames["results"]
            with open(input_file) as fin:
                self._results[system] = fin.read().strip() == "0"

    @property
    def results(self):
        """Getter for the 'results' attribute."""
        if not self._results:
            self.read_results()
        return self._results

    @property
    def logs(self):
        """Getter for the 'logs' attribute."""
        if not self._logs:
            self.read_logs()
        return self._logs


if __name__ == "__main__":
    # execute only if run as a script
    smoke_tests = SmokeTests()
    print("Results:")
    print(smoke_tests.results)
    print("Logs:")
    print(smoke_tests.logs)
