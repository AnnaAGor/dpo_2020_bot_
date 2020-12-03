token = '1413386374:AAHDlVvaHph1NRT6PXvYluxkjyuor9Y2Cjs'

from enum import Enum

db_file = 'database.vdb'

class States(Enum):
    S_START = "0"
    S_INTRODUCTION = "1"
    S_NEWERA_OR_OLDSCHOOL = "2"
    S_ENTER_WHICH_DOCTOR = "3"
    S_ENTER_MORE_INFO = "4"
