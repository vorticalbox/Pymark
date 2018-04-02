# Pymark
Pymark is a simple python based benchmark that uses pools and Pythagoras Theorem to give an idea of CPU speed. It returns a time in seconds for single then max threads. 

You can use this as an example of how to use pools.

## Installation

Python 3 is required. Pymark will not run using Python 2.

To install it, put in a folder and import or run as is

## Usage

if importing

startInt(n)
n = number of calculation, 10**7 (10 million) is suggested to avoid memory errors

startFloat(n)
n = number of calculation, 10**4 (10,000) is suggested due to time to calculate. 
limited to 4 cores or more due to time. 

i(list)
This is the function that does all the int calculations and it takes a list. no need to use this function as it is called from startInt()

f(list)
This function does float calculations and takes a list. No need to use this function as it is called from startFloat()

## TODO
-Output results to file
-Create more tests

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
###v1.3
1. Massively reduced memory usage.
2. Changed Float to allow testing on any system.
3. Much neater code


###v1.2
1. Added Float test for CPUs with 4 threads or more
2. Fixed an issue to left the list populated between tests, now clears list at the end of each test.

###v1.1
1. added auto thread detection

###v1.0
1. Created basic benchmark.

## Credits

@vorticalbox

## License

Pymark is licensed under the MIT License which can be found in the LICENSE.md file in this repository.
