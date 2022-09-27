# CS425_MP2_LiYao



## Getting started
Under the src folder 
Start with VM1, which is the introducer, on the command line
```
sudo ./commands.sh "join" 
```
to initialize the ring.

## Join the membership 
On any machine after the introducer(VM1) is initialized, use
```
sudo ./commands.sh "join" 
```
again to join the membership.


## Check the memebership
On any machines that currently active, use
```
sudo ./commands.sh "list_mem" 
```
to see the currently enrolled membership list.
## Check the Predecessor & Successor of the Current Machine
For the predecessor
```
sudo ./commands.sh "list_pred" 
```
To check the id, IP address, timestamp of the predecessor of the current machine.
Similarly, for the first successor and second successor
```
sudo ./commands.sh "list_succ1" 
```

```
sudo ./commands.sh "list_succ2" 
```

## Refer to the log
Any update of the membership list would be automatically recorded in the "ActivityRecord.log". In the Commandline
```
grep "FROM" ActivityRecord.log
```
To get access to every record of the log.



