from .errors import Errors

# // Table class
class Table(object):
    def __init__(self, columns: int = 0, headers: list[str] = [], data: list[any] = []) -> None:
        self.headers = headers
        self.columns = columns
        self.data = data
        
    def __str__(self) -> str:
        if len(self.data) < self.columns:
            return Errors.critical(f"Not enough data in table with '{self.columns}' columns!")
        
        if self.columns > 0:
            self.data = self._split_data(self.data)
            return (
                "\\begin{tabular}{" + "".join('|c' for _ in range(self.columns)) + "|}\hline" + 
                self._headers() + 
                self._body() + 
                "\\end{tabular}\\leavevmode\\\\"
            )
        Errors.warning("Table is empty. (0 columns)")
        return ""
        
    def _split_data(self, data: list[any]) -> list[any]:
        return [data[x:x + self.columns] for x in range(0, len(data), self.columns)]
    
    def _headers(self) -> str:
        for i in range(len(self.headers)):
            if i != len(self.headers) - 1:
                self.headers[i] = f"{{{self.headers[i]}}}&"
            else:
                self.headers[i] = f"{{{self.headers[i]}}}\\\\\\hline"
        return "".join(h for h in self.headers)
    
    def _body(self) -> str:
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j != len(self.data[i]) - 1:
                    self.data[i][j] = f"{{{self.data[i][j]}}}&"
                else:
                    self.data[i][j] = f"{{{self.data[i][j]}}}\\\\\\hline"
        return "".join("".join(a for a in b) for b in self.data)
