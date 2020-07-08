import re

time = "PT31H21M25S"
re.sub(r"[#%!@*]", "", time)
