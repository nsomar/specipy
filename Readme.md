[![Build Status](https://travis-ci.org/oarrabi/specipy.svg)](https://travis-ci.org/oarrabi/specipy)

# Specipy

Ever wanted to check how your Kiwi specs would read out loud, or you wanted to share your spec with your teammates.   
Specipy helps into parsing a kiwi spec file to human readable format, allowing you to have a higher picture on which parts your tests covers.

Using specipy helps raising the tests abstraction layer when testing, and helps moving forward with writing tests.

## Installation
First [install pip](https://pip.pypa.io/en/latest/installing.html) if you don't have it. 

Install specipy with pip:

	pip install specipy

## Usage
Specipy is used as following:

	specipy <path_to_spec_file>
	
A kiwi spec would look like this:

	--------------------------------------------------
	Describe: The first describe
	--------------------------------------------------

	    When: first context
	        It: has this test
	        It: and a second test

	        When: inner context
	            It: has this an inner test
	            It: and a second inner test

	    When: second context
	        It: has this othertest

	--------------------------------------------------
	Describe: The second describe
	--------------------------------------------------

	    When: second descibe context
	        It: has this other test
	        It: and another test

## Tests
Sure, [tests](https://github.com/oarrabi/specipy/tree/master/tests) cover all the possible parsing situations.

## Contributing

1. Fork it ( https://github.com/oarrabi/specipy/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

