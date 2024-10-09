# Illumio - Take Home Assessment (by Rohan Ghosalkar)

Date: 8th October, 2024

## Description

The repository contains code to parse an input file containing flow log data, which is then mapped according to a lookup table. The code is written in Python. I have used the terminal on MacOS and my IDE was VSCode. Below are instructions to run the code. I have also included some test cases and the assumptions that were made. 

For more information or if you have any issues in running the program, please contact rghosalk@ucsc.edu. 

## To run the program 

Please make sure that you have Python installed on your device. You can find instructions [here](https://realpython.com/installing-python/). 

1. open the terminal on your computer.
2. if you have any additional input files, move them into the __input__ folder. Please note this repository already has input files (similar to example given in the problem statement)
3. ignore if you are in the directory with the main code. if you are in the root dir, then type the following command. :
```
cd path_to_illumio-takehome-rpg
```
4. create a virtual environment to run the code
```
python -m venv venv
source venv/bin/activate
```
6. run the main code
```
python main.py input/<logs_filename>.txt input/<lookup_filename>.txt
```
if you want to use the already added input logs use the following command
```
python main.py input/logs.txt input/lookup.txt
```
7. run the test
```
python -m unittest testing/test_main.py
```
8. exit the environment
```
deactivate
```

## Requirements

- input files are plain text files (ascii) but the lookup file can also be csv
- the flow log size can be up to 10 mb
- the lookup file can have up to 10000 mappings
- the tags can map to more than one port/protocol combination
- the matches are case sensitive

## Assumptions

- only default format and version 2 fields are supported. therefore, each log would have 14 fields
- the input logs are in string format in the txt file. each field is separated by a space.
- we list the output for every tag when it is more than 0. same for the port/protocol matches (based on the example). tags and port/protocol combinations that have 0 counts are not mentioned in the output
- the protocol numbers considered are mentioned [here](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). the current ones include icmp, tcp, udp, igmp, ipv4, igmp, stp, smp and ospfany. any additional ones are considered invalid. you can change this in the __matcher.py__ file in the __modules__ dir.
- every port/protocol combination maps to a single tag only. i.e. two port/protocol combinations can have the same tag, but one combination cannot have two tags
- the problem statement mentions that the lookup table is a csv file in the beginning however, the requirements mention that both input files are txt. the code works for either one, as long as the path to both the input files is mentioned appropriately
- the program prints the output, but also generates two txt files as the output (tag_counts & port_protocol_counts)

## Tests

- improper commands or incomplete arguments (prints correct syntax)
- improper files:
    - empty files (prints error message)
    - nonexistent files (prints error message)
- improper logs (prints error log, continues parsing for rest)
- invalid protocol number (prints out the error log, continues parsing for rest)
- no logs mapped to tags (empty output)
- multiple port/protocol pairs (output with aggregated values)

Further testing can be done on large files. 
