# Manual Scoring of Stimuli Testing Result Program

This program is to produce a result of a stimuli testing program with a manual scoring option. 
It reads a .txt file produced by previous stimuli-testing program (FixedStimuli, FixedStimuli2) and calculates the score of each factor from a PostgreSQL database called 'score'.
The stimuli-testing programs are not uploaded in here but you can find from CMU Socius Research Team or email me (siheonl@andrew.cmu.edu) if you are a member of Socius.

There are four versions of programs. If a testing result file is from FixedStimuli, run one of '_old.py' files. If a result file is from FixedStimuli2, run one of '_new.py' files.
If the participant of a stimuli testing put different scores on total donation for each donation type, run one of '_total_.py' files

If you want to run a different result file, rename the text files with 'pid_old.txt' or 'pid_new.txt' and place in a 'textFiles' folder

## Getting Started

Before starting this file you need

```
PostgreSQL
plpgsql(python library for integrating PostgreSQL to a python file)
```
email me (siheonl@andrew.cmu.edu) to request updated csv files for load_data.sql

### Process

1. Open terminal and go to the directory where the git is located

2. run PostgreSQL

```
$ psql
```

3. Create PostgreSQL database 'score'

```
# CREATE DATABASE score;

# \q
```

4. At the directory, run load_data.sql file

```
$ psql -U username -d score -f load_data.sql 
```

5. run a program with a correct version (new/old, total/non-total)

```
$ python filename.py
```

6. The resulted files would locate at the directory


## Built With

* [Python](https://www.python.org/) - plpgsql library
* [PostgreSQL](https://www.postgresql.org/docs/9.6/static/plpgsql.html) - Database

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Siheon Lee** - *Initial work* - [Socius](https://github.com/leesihoney)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under CMU Socius


