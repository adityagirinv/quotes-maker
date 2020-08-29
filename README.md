# QuotesMaker
QuotesMaker.py is a python based quotes to image converter. You can convert either one quote or pass a file containing quotes it will automatically create images for those quotes using 4 templates that are pre-built. If you want more templates you can request us here.

## Templates

We will add more template if we get enough requests

- ***Template #1***
[![Template 1](https://i.imgur.com/k4q5pVP.jpg)]()
- ***Template #2***
[![Template 2](https://i.imgur.com/qrVVwHb.jpg)]()
- ***Template #3***
[![Template 3](https://i.imgur.com/1yNu4VY.jpg)]()
- ***Template #4***
[![Template 4](https://i.imgur.com/i7thu2L.jpg)]()
- ***Template #5***
[![Template 5](https://i.imgur.com/DagMkn3.jpg)]()
- ***Template #6***
[![Template 6](https://i.imgur.com/jvdN8d1.jpg)]()
- ***Template #7***
[![Template 7](https://i.imgur.com/i8LVSxw.jpg)]()


## Requirements
>Our program uses Pillow as a additional module to function.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pillow.
```bash 
pip install -r requirements.txt
```
## Usage 
To access help menu run
```bash
quotesmaker.py -h
```
There are two modes you can create quotes
- Manual
- Passing a .txt file
### Adding a logo for watermark
Our code only support's .png format. You can find tons of image format converter online if this is a issue for you.

### Manual 
> Passing a quotes manually would look something like code below.

```bash
quotesmaker.py -q "Your Quote Goes Here" -a "author(optional)" -t 1 -l test_logo.png
```
>If you don't pass Author (-a) That place will be left vacant.

>If you don't pass Template number from 1-4 (-t) random will be choosed.

>If you don't pass logo (-l) quotes mark will appear at top right corner.

```bash
quotesmaker.py -q "this is my quote"
```
### Passing a .txt file
You can pass a .txt file by running

```bash
quotesmaker.py -f filename -s separator -t 1 -l test_logo.png
```
where Filename is full directory of your file.

A separator can be better understood with following example.
```
this is my thought[place for separator]Name of author
this is my thought no.2 [place for separator]Name of 2nd author
```
Lines above is a typical example of a .txt file containing quotes.
So, Now you can understand that separator is a unique set of character between quotes and it's author in each line.

While You are using [-f] in quotesmaker.py if you don't provide [-s] the default separator will be set to ``` . You can also pass Your own logo to add watermark but this is optional.

***We recommend you Not to use [-t] while you are using [-f] as it will automatically choose random template for each quote which makes it more fun***

So finally command would look like
```bash
quotesmaker.py -f test_quotes.txt -s ``` -l test_logo.png
```

***We have also added a test logo[test_logo.png] and a test quotes [test_quotes.txt] file to play and learn how to use this tool though the logo is property of @real_quoter in instagram so, you are not allowed to use it.***

## Errors

***Error:001***

[-q and -f both not provided]
You have to provide at least one of them to continue using program see [-h] for help.

***Error:002***

[-q and -f both provided] 
You have to provide one of them either [-q] or [-f] see [-h] for more info.

***Error:003***

[-l logo is not .png format] 
Our code currently only supports .png format. Please Use some image format converter online to fix this issue

***Error:004***

[logo file doesn't exist] The logo file that you specified doesn't exists in that directory kindly check it one more time.

>If you think this is a error of our code kindly report us in Github

***Error:005***

[specied -f file doesn't exists] The txt file you provided doesn't exists in that directory please check that directory.

>If you think this is a error of our code kindly report us in Github


## Contribution

This code is fully written by adityagirinv and support by @Lablnet to fix many issue. If you wish to co-operate with me or send an suggestion contact me on ***geotics.yt@gmail.com***

## LICENSE

### LICENSE.txt

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 adityagirinv

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
