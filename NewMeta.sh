apk --no-cache add py2-pip python-dev
pip install sphinx
apk --no-cache add make
make html
mv _build/html/ public/


