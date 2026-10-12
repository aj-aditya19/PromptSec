# Data fixes applied before analysis
1. Removed `__pycache__` folders and one stray `requirements.txt` (ChatGPT/synonym).
2. Renamed folder `Claude/orginal` -> `Claude/original`; `GitHub-Copilot` -> `Copilot`.
3. Gemini/typo/task18.py: the copy from chat turned the escape sequences "\n" and "\r" inside
   `username.replace(...)` into real newline characters, so the file did not parse. Restored the escapes.
   (Formatting repair only; confirm against the original chat.)
