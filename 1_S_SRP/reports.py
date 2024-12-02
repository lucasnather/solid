from abc import abstractclassmethod, ABC

class ReportsInterface(ABC):

    @abstractclassmethod
    def generate_report(message: str) -> str:
        pass

    @abstractclassmethod
    def send_report() -> str:
        pass

class Reports(ReportsInterface):

    def generate_report(message: str):
        return f"Your report {message}"

    def send_report(self):
        return self.generate_report()