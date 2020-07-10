# Mode Randomizer

A very simple Python script that randomizes all possible
(Mode, Key, String-Crossing) triplets for the 4-string bass guitar
to provide the user with a randomized challenge to test their command of 
musical modes.

Very easy to switch to extended range bass guitar, standard 6-string guitar,
and any other stringed instruments where playing modes across different string crossings
is something that makes sense. For example, to add the low B string of the 5-string bass guitar,
all one needs to do is change the list `strings` from   

`strings = ["E", "A", "D", "G"]`

to 

`strings = ["B", "E", "A", "D", "G"]`

However, in any extended range bass guitar (5 strings and above) there is no need
for a position switch on any string, since the existence of one more string
covers the notes that we would need to switch for on the 4-string. A 5/6/7...
string player might be interested in modifying the script so that it calls the method 
method `get_random_mode_and_key()` instead of the more general `get_random_mode_key_and_string()`. 
## Licensing

GPL3. Refer to attached LICENSE file.

## Contributing / Comments

Do a pull request on the repo, or [contact me over e-mail](mailto:jason.filippou@gmail.com).

