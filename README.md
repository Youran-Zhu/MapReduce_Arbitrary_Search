# MapReduce

This repo provides two examples and a script to easily define and run mapper and reducer functions against Hadoop MapReduce.

Generally speaking, on the top level there are folders that must contain:

* mapper.py
* reducer.py
* sample directory with data to be copied in hdfs within docker container

__ENSURE THAT .py FILES HAVE `chmod +x` PERMISSIONS__
(This is hadoop requirement)

Of course, the idea is to add more folders that demonstrate different aggregations that can be achieved with MapReduce over different datasets (that are available in the sample folder). The aspiration was to make something reusable quickly and cheaply.

## Usage

1. Download this repo
2. CD into this repo
3. Run the following

```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh basic_grep
```
(notice the **basic_grep** keyword at the end - corresponds to the folder **basic_grep**!)

expected output:

```
foo	6
quux	4
```

Another example:

```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh count
```
(notice the **count** keyword at the end  - corresponds to the folder **count**!)

expected output:

```
bar	0
foo	6
labs	0
quux	4
```
## Generalization
The folder **grep** provide code that we could use to manage __any__ type of search. In this case, our search criterias should be encoded in RegEx format and provided as commendline inputs. For example, if we want to find all the words that start with "f" or end with "d", we could run the following:

```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh grep f.* .*d
```
Notice:
  1) The **grep** keyword - corresponds to the folder **grep**
  2) The **f.*** keyword - corresponds to "all the words that start with 'f' " in RegEx 
  3) The **\.\*d** keyword - corresponds to "all the words that end with 'd' " in RegEx 
  4) We could add as many RegEx criteria as we want. These criteria are connected by logic "Or". In other word, it will find all the words that conform to any one of these criteria. 
