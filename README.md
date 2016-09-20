# Pymark

Pymark is a simple benchmark that uses pools and Pythagoras Theorem to give an idea of CPU speed. It returns a time in seconds for each thread count used. 

You can use this as an example of how to use pools.

## Installation

Put in a folder and import or run as is

## Usage

if importing

stratInt(n)
n = number of calculation, 10**7 (10 million) is suggested to avoid memory errors

startFloat(n)
n = number of calculation, 10**4 (10,000) is suggested due to time to calculate. 
limited to 4 cores or more due to time. 

f(list)
This is the function that does all the calculations, it takes a list. no need to use this function as it is called from startBench()

## TODO
-Output results to file

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
v1.2
Added Float test for CPUs with 4 threads or more
Fixed an issue to left the list populated between tests, now clears list at the end of each test.

v1.1
added auto thread detection

v1.0
Created basic benchmark.

## Credits

@vorticalbox

## License

MIT License

Copyright (c) 2016 vorticalbox

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
