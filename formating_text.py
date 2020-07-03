import datetime
import re

import dateutil.parser


time = "PT31H21M25S"
re.sub(r"[#%!@*]", "", time)
