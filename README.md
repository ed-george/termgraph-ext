termgraph-ext
=============

An extension to Marcus Kazmierczak's `termgraph` which draws basic graphs in the terminal

The original repo is located [here](https://github.com/mkaz/termgraph)

### Authors
Ed George, [Website](http://edgeorgedev.co.uk) - [Twitter](https://twitter.com/edgeorge92)

Marcus Kazmierczak, [Website](http://mkaz.com/)


### Examples

`$ python termgraph-ext.py -c -d -p ex.dat`

<img src="https://raw.github.com/ed-george/termgraph-ext/master/example.png">


### Usage

* Create data file with two columns either comma or space separated.
  The first column is your labels, the second column is numeric data

`$ python termgraph-ext.py [datafile]`

A full overview of current features are documented below:

```
usage: termgraph-ext.py [-h] [-c] [-d] [-f FORMAT] [-p] [-w WIDTH] [-v]
                       filename

draw basic graphs on terminal

positional arguments:
  filename              data file name (comma or space separated)

optional arguments:
  -h, --help            show this help message and exit
  -c, --color           print graph using ANSI color
  -d, --diff            show numerical difference between adjacent plots
  -f FORMAT, --format FORMAT
                        specify date format used in data labels
  -p, --parse           parse date format used in data labels
  -w WIDTH, --width WIDTH
                        width of graph in characters default:50
  -v, --verbose
```
