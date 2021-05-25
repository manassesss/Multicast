# Multicast 
This repository contain a solution to an exercise proposed by the professor in discipline of Distributed Systems.
In this solution it was used Python 3.7.7

## :memo: Exercise 
Development of a fault-tolerant application
Create an application that allows you to solve simple arithmetic expressions. The client must send a request, via IP multicast, an arithmetic expression (Ex: 3 + 5-4 / 3 * 4) to a group of servers. These servers must have unique identifiers from 1 to n, where n is the number of servers. You must respond to the client, the server with the lowest identifier that is available.

Servers must periodically exchange multicast messages with each other to verify that they have failed. In case of failure of the server with the lowest id, the second with the lowest id must respond to the client, and so on.

A compressed file containing the application's source code, file containing execution instructions and a report with details of how it was implemented and the results obtained must be sent.

## :computer: The virtual machines 
The professor provided 4 virtual machines already configured. Those virtual machine was used in the [VirtualBox](https://www.virtualbox.org/). The version used in this work was 6.1.

Before use directly the code in the virtual machines you need to config the share folders to use the folder that contains your codes. To do that, access the settings of the virtual machine and after click on tab Shared Folders and add the folder with your codes! Make sure that the build option is marked.

All the machines used is this work had Ubuntu Operational System installed

## :snake: Python
The version used in this work was the 3.7.7 version. You can download Python [here](https://www.python.org/downloads/)

## :hammer_and_wrench: How to execute

Start the machines you are going to use, and execute, first, the Sender.py code:

`python3 Sender.py`

and after that, execute the Receiver.py in the other machines:

`python3 Receiver.py`

