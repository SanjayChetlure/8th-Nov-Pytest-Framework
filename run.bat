@echo off
call ".venv\Scripts\activate.bat"
pytest -v -s Test_Cases/SwagLoginTest.py --browser="edge" --html=Reports/SwagLabs1.html
Pause
