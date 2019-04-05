pip install sphinx
cd ./Sphinxter
printf 'y\ny\ny\ny\n\n\n\n' | sphinx-quickstart
make html
mv build/html/ public/
ls

