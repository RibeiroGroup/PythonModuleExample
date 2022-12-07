# PythonModuleExample

A minimal example of a Python module suitable for research. 

The structure of this module is
```
PythonModuleExample/
├── data
│   ├── benzene
│   │   ├── output.dat
│   │   └── run.py
│   └── water
│       ├── output.dat
│       └── run.py
├── LICENSE
├── nuclear
│   ├── __init__.py
│   └── main.py
├── README.md
└── tests
    └── test_nuclear.py
```

# Features of this example

- Code and data are separated: `nuclear` host the source code whereas
`data` holds the actual data generated from it. The `data` folder may be
used to store research data generated in your project without comprimising the 
readability and organization of the source code.

- All functions are docummented by docstring. Moveover, comment are present throughout
the code.

- Tests are included for all functions and can be perform by running `pytest`. Ideally, you 
would setup a continuous integration scheme to make sure that tests are run every time
the code is changed.

- `LICENSE` contains relevant legal information for people who want to use, copy, modify or distribute your code
In a research enviroment, we generally choose permissive licenses such as BSD-3 and MIT.

- `README.md`, such as the file you are reading right now, is normally used for instructions on how to obtain,
install, and run your code. 


# Running tests

To run tests and check coverage you will need specific packages, here we will use `pytest` and `coverage`.
They can be installed with pip
```
$ pip3 install pytest
$ pip3 install coverage
```

Run tests as
```
coverage run -m pytest 
```
To check coverage run
```
coverage report
```
