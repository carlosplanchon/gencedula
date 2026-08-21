# gencedula

![gencedula — check digit utilities for Uruguayan cédulas in Python](https://raw.githubusercontent.com/carlosplanchon/gencedula/master/assets/gencedula_banner.jpg)

*Generate and verify Uruguayan identity document numbers.*

Zero runtime dependencies. Handy for generating valid test data:
the uruguayan *cédula de identidad* is not covered by
[python-stdnum](https://arthurdejong.org/python-stdnum/) (which only
ships the uruguayan RUT), and validators don't generate numbers anyway.

A generated number is only *checksum-valid*: it passes the
verifier-digit algorithm, but that does not mean it was ever issued,
and it may coincide with a real person's number. `verify_cedula`
likewise checks the verifier digit only, not whether the document
exists.

## Installation
### Install with uv
```
uv add gencedula
```

## Usage
```
In [1]: import gencedula

In [2]: for x in range(10):
	print(
		gencedula.generate_cedula(
			start=4_000_000,
			stop=5_000_000,
			step=200
			)
		)
46308006
47486005
49378000
41064007
40756005
45282003
47958004
44844000
41564007
49684003

In [3]: gencedula.verify_cedula(46308006)
Out[3]: True

In [4]: gencedula.verify_cedula(46308007)
Out[4]: False

In [5]: gencedula.calculate_digito_verificador(4630800)
Out[5]: 6

In [6]: gencedula.format_cedula(46308006)
Out[6]: '4.630.800-6'
```

## Tests
```
python -m unittest discover tests
```
