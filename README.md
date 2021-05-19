# Multicast
This repository contain a solution to an exercise proposed by the professor in discipline of Distributed Systems.
In this solution it was used Python 3.7.7

## Exercise
Development of a fault-tolerant application
Create an application that allows you to solve simple arithmetic expressions. The client must send a request, via IP multicast, an arithmetic expression (Ex: 3 + 5-4 / 3 * 4) to a group of servers. These servers must have unique identifiers from 1 to n, where n is the number of servers. You must respond to the client, the server with the lowest identifier that is available.

Servers must periodically exchange multicast messages with each other to verify that they have failed. In case of failure of the server with the lowest id, the second with the lowest id must respond to the client, and so on.

A compressed file containing the application's source code, file containing execution instructions and a report with details of how it was implemented and the results obtained must be sent.

## How to execute
