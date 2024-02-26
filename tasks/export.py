from typing import List, Tuple
from openpyxl import Workbook


def save_to_file(tasks: List[Tuple[int, str, bool]], file_name: str) -> None:
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    # Data can be assigned directly to cells
    ws.append('Index', 'Title', 'Completed')

    # Rows can also be appended
    for task in tasks:
        ws.append(task)

    # Save the file
    wb.save(f"./out/{file_name}.xlsx")