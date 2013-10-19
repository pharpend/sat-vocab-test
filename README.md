# sat-vocab-test

This is a vocabulary study tool I wrote for myself a few years ago. I
uploaded here at a friend's request. 

You are welcome to do with it as you please, as long as you comply with
the license (see the file called LICENSE). 

# Usage

This program requires Python 2, numpy (for sorted searching) and SQLite
3.

If you want a definition-based quiz, that is, a quiz that gives you a
definition, and then asks you for a word:

```zsh
python2 sat_def_based_quiz.py
```

If you want a word-based quiz, that is, a quiz that gives you a word,
and asks for the corresponding definition:

```zsh
python2 sat_word_based_quiz.py
```

# Sample output

```
$ python2 sat_def_based_quiz.py
How many questions? 5

--
1. What is the best word for 'To divide.'?
* predict
* relinquish
* quadrate
* beget
* dissever
Answer ('x' to exit): dissever
Correct answer is "dissever"
(1/1) (100 percent) (A)

--
2. What is the best word for 'To hurry.'?
* assimilate
* irritate
* inhume
* underman
* bustle
Answer ('x' to exit): bustle
Correct answer is "bustle"
(2/2) (100 percent) (A)

--
3. What is the best word for 'The period of time during which anything
lasts.'?
* antonym
* duration
* conscience
* reticence
* excitation
Answer ('x' to exit): duration
Correct answer is "duration"
(3/3) (100 percent) (A)

--
4. What is the best word for 'Showing or expressing a deficiency of
veneration, especially for sacred things.'?
* truthful
* gigantic
* reverent
* irreverent
* inveterate
Answer ('x' to exit): irreverent
Correct answer is "irreverent"
(4/4) (100 percent) (A)

--
5. What is the best word for 'A number of persons secretly united for
effecting by intrigue some private purpose.'?
* avalanche
* gastronomy
* apostasy
* martyrdom
* cabal
Answer ('x' to exit): apostasy
Correct answer is "cabal"
(4/5) (80 percent) (B-)
You got 4 correct out of 5 (80 percent) (B-)
Press [Enter] to quit.
```

```
$ python2 sat_word_based_quiz.py 
How many questions? 3

--
1. What is the definition of 'technology'?
0.  Expansion.
1.  A member of a regiment composed of men of great stature.
2.  The knowledge relating to industries and manufactures.
3.  A tomb of more than ordinary size or architectural pretensions.
4.  A small dagger.
Answer ('exit' to exit): 2
Correct answer is The knowledge relating to industries and manufactures.
(1/1) (100 percent) (A)

--
2. What is the definition of 'hydrous'?
0.  Deepest within.
1.  Of or pertaining to Sir Isaac Newton, the English philosopher.
2.  Watery.
3.  Untenable.
4.  Moved or managed with difficulty, as from great size or awkward
shape.
Answer ('exit' to exit): 2
Correct answer is Watery.
(2/2) (100 percent) (A)

--
3. What is the definition of 'pertinacious'?
0.  Not flowing: said of water, as in a pool.
1.  Persistent or unyielding.
2.  Easily led or controlled.
3.  Fit to be compared.
4.  Unrelenting.
Answer ('exit' to exit): 1
Correct answer is Persistent or unyielding.
(3/3) (100 percent) (A)
You got 3 correct out of 3 (100 percent) (A)
Press [Enter] to quit.
```
