# Exam 1: Flight Traveler Tracker

## Description

Write a Python program that reads a file containing flight details and keeps track of the number of countries visited by each person. The program should be able to read flight records from a file, group travelers by name, and count the unique countries they have visited. The output should list each traveler along with the countries they have visited and identify the person who has visited the most countries.

## Tasks

1. Implement the function `readFlights(filename: str)` that reads the flight details from a file named `flights.txt`. Each line in the file contains a traveler's name followed by a country they've visited, separated by a space.
2. Implement the function `groupTravelers(flights: list[str])` that groups the travelers by their names and records the unique countries they have visited.
3. Implement the function `printTravelers(travelers: list)` that prints the list of travelers and the countries they've visited, sorted alphabetically by name.
4. Implement the function `getPersonWithMostCountries(travelers: list)` to find the traveler who has visited the most countries.

## Input Format

The input file `flights.txt` contains multiple lines with the following format:

```
Name Country
```

## Output Format

The output should list each traveler's name followed by the countries they have visited, sorted alphabetically, and then state the name of the person who has visited the most countries and the number of countries visited. For example:

```
Anna:
    Canada
    Iceland
    Italy
Gunnar:
    Germany
    Iceland
Anna has been to 3 countries
```

## Sample Input File `flights.txt`

```
Anna Iceland
Gunnar Germany
Anna Canada
Gunnar Iceland
Anna Italy
```

## Execution

To execute the program, the user will be prompted to enter the filename:

```
Enter filename: flights.txt
```

After the program processes the input file, it will print the travelers and their visited countries, followed by the person with the most countries visited.

---

# Exam 2: Soccer Team Player Tracker

## Description

Create a Python program that manages soccer players and their teams. The program should be capable of tracking the number of games and goals for each player and calculate their average goals per game. Additionally, it should manage teams, adding players to teams, and determine the top goal scorer in each team.

## Tasks

1. Complete the `Player` class with an initializer, methods to add a game, calculate the average score, and a string representation of the player's details.
2. Complete the `Team` class with an initializer, a method to add players to the team, and a method to determine the top goal scorer.
3. In the `main` function, create instances of `Player` with given details, add games and goals to some players, and then create instances of `Team`, adding players to them.
4. Print the details of each player and the team they belong to, along with the top goal scorer for each team.

## Input Format

No input file is required. The program will create instances with predefined data.

## Output Format

The output should list each player's details and the team they belong to, followed by the name of the top goal scorer in each team. For example:

```
Player: Gunnar Jónsson
Team: Keflavík
Games: 18
Goals: 6
Average goals per game: 0.33
...
Team: Keflavík
Gunnar Jónsson
Guðmundur Einarsson
Goal scorer: Gunnar Jónsson
```

## Execution

The program is executed with the `main()` function, which will print the details of each player and the top goal scorer of each team.

---

## Instructions for Students

- Read the description and the tasks carefully.
- Make sure to follow the input and output formats as specified.
- Write your code in a manner that is easy to read and understand.
- Include comments in your code to explain your logic.
- Test your program thoroughly to ensure it behaves as expected.
- Submit your `.py` file and the README.md file with the instructions and description of your program.

Good luck!
