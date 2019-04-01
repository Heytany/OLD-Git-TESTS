pip install --upgrade pip
pip install pycodestyle
pycodestyle *.py

pip install sphinx
cd ./Sphinxter
printf 'y\ny\ny\ny\n\n\n\n' | sphinx-quickstart
sphinx-build -M html source build