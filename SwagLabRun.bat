@echo off
call env\Scripts\activate
pytest -v -s Test_Cases/SwagLoginTest.py --browser="edge" --html=Reports/SwagLabs1.html -m "sanity"
pause
