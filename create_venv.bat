cmd /C
python -m venv .venv &
cd .venv\Scripts\
start activate.bat
python.exe -m pip install --upgrade pip &
pip list &
pip install django