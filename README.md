### simple letters converter

![pytests](https://github.com/michalswi/letters-converter/actions/workflows/tests.yml/badge.svg)  

Convert letters in specific file to ASCI chars.

```
$ echo -e "line1 ąę\nline2 ćź" > /tmp/demo.txt

$ cat /tmp/demo.txt
line1 ąę
line2 ćź

$ python3 convert.py /tmp/demo.txt
Letters converted..

$ cat /tmp/demo.txt
test ae
test2 cz
```