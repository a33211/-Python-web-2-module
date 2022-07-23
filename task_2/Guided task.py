class AbstractView(ABC):
    @abstractmethod
    def showRecords(self):
        pass

    @abstractmethod
    def showSingleRecord(self, key):
        pass


class ContactBookView(AbstractView):

    def showRecords(self):
        pass

    def showSingleRecord(self, key):
        pass


class NotebookView(AbstractView):
    def showRecords(self):
        pass

    def showSingleRecord(self, key):
        pass