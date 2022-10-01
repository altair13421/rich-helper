from rich.table import Table
from rich.console import Console
import time
from random import random
from typing import Dict, List

class Rich_helper:
    """Rich Helper Class
    rprint_error(string) - will Return beautified String for error message
    rprint_log(string) - will Return beautified String for log message
    rprint_success(string) - will Return beautified String for success message
    sleeper(timer) - sleeps
    table_printer(columns, data) - will print a table using rich.table library
    progress_bar() - will add a Progress bar Later
    """
    def __init__(self):
        self.console = Console()
    def rprint_error(self, string):
        self.console.log(f'[red] Error:[/red] [light_pink4]{string} [/light_pink4]')
    def rprint_log(self, string):
        self.console.log(f'[cyan] Progress:[/cyan] [sky_blue1]{string} [sky_blue1]')
    def rprint_success(self, string):
        self.console.log(f'[green] Success:[/green] [aquamarine1]{string} [/aquamarine1]')
    def sleeper(self, timer):
        time.sleep(timer)
    def table_printer(self, columns: List[str], data: List(Dict)):
        table = Table(title="Recent News")
        styles = ["red", "cyan", "green", "magenta", "aquamarine1", "light_pink4", "sky_blue1"]
        for column in columns:
            table.add_column(column, justify="right", style=styles[random.randint(0, len(styles)-1)])
        for item in data:
            table.add_row(item[column] for column in columns)
        self.console.print(table)
    def progress_bar(self,):
        pass
