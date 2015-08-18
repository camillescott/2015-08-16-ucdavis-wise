Copy and paste last cell into a file called calc_stats_for_patients.py and save to python folder

Add: import numpy, import glob


Start ipython interrpreter

Show how to import libraries, math, etc without the notebook


>>>import calc_stats_for_patients


Then exit the ipython interpreter


python calc_stats_for_patients


(should see the same thing)


Now add if __name__ == “__main__”:

python calc_stats_for_patients


Start the ipython interpreter

>>>import calc_stats_for_patients


Nothing happens


Now you can call the function

calc_stats_for_patients.main([‘data/inflammation-01.csv’], ‘max’)


Now add command line arguments


add import sys

add print 'sys.argv returns: ', sys.argv under if __name__ == “__main__”

comment out call to main

python calc_stats_for_patients arg1, arg2, arg3


Assign the first argument to be the action and the rest to be the filenames

uncomment main

modify main to accept file_list and action


Exercise:

Modify your script to also take single letter arguments (n for min, x for max, and m for mean)


If time - add testing

	assert that action is one of the values

	assert file list isn’t empty

	break if statements into a separate script

	add docstring



