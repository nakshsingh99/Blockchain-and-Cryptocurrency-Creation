### Blockchain-and-Cryptocurrency-Creation

## Create a Simple Blockchain

**To be installed:**

- Flask==0.12.2: pip install Flask==0.12.2
- Postman HTTP Client: https://www.getpostman.com/

**STEPS:**

**Import the libraries**

**Building a Blockchain**

- Initialize list for containing different blocks
- Creation of Genesis Block i.e First block of blockchain
- Now we will append different blocks that will be mined together in the empty list
- Getting the last block of current chain
- Defining PoW for miners to solve
- Number of leading zeros increase hardness of problem for miners to solve
- Checking if everything is right in blockchain. I.e check for PoW and if prev\_hash= hash of previous block
- Creation of Hash function

**Mine our Blockchain**

**Create a Web App**

**Creating a Blockchain**

- Mining a new block
- route() decorator to tell Flask that what URL should trigger our function
- Getting the Proof of work function
- Call create block function to append the newly mined block
- Getting the full Blockchain
- Checking if the Blockchain is valid
- Running the app

## Create a Crypto Currency

**To be installed:**

- Flask==0.12.2: pip install Flask==0.12.2
- Postman HTTP Client: https://www.getpostman.com/
- requests==2.18.4: pip install requests==2.18.4

**STEPS:**

**Import the libraries**

**Building a Blockchain**

- Create a class blockchain and copy all the function from creating a blockchain code
- Add few more functions to the class:
- Add Transaction
  - Add transaction to the blockchain we will need sender receiver and amount to be sent and this info is added to the list during transaction
  - Then we get the prev block and get its index
- Replace Chain
  - Replace chain if there exist another chain longer then the chain related to the node
- Add node
  - To add a node to the cryptocurrency world we need parse the url in order get the netloc
  - Address: &#39;https://120.0.0.1:5000/&#39;
  - Parsed URL: (schema= &#39;http&#39; netloc= &#39;120.0.0.1:5000&#39;...)

**Mining a Blockchain**

- Create a Web App
- Create an address for the node on Port 5000
- Create a Blockchain
- Add all the routes from the blockchain file.

**Decentralize The Blockchain**

- Add new routes to the file such as:
- Connect nodes.
  - Create a json file of all nodes and connect it to a code file.
  - Add the nodes present in JSON files to the cryptocurrency world.
- Add transaction
  - Create a json file with all three keys of the transaction and connect it to the code file.
  - Add the keys to the transaction.
- Replace Chain
  - Use replace Chain function from the class and execute it in the route/\.
- Run the app

## Three Procoin file:
- More than one node is needed for transaction.
- In blockchain, the three codes represent three different nodes in the cryptocurrency world.


## Postman Steps

After the code is compiled to test the blockchain we need to go to postman or any other environment of choice and type the url &quot;[http://127.0.0.1:5000/](http://127.0.0.1:5000/)&quot; and then append different end-point to perform different functions:

**/mine\_block:** To mine a new block and add it to block chain

**/get\_chain:** To get the blockchain created so far

**/is\_valid:** To check the blockchain if it is valid or not.

**/connect\_nodes:** To connect the nodes in the cryptocurrency world.

**/add\_transaction:** To add transaction.

**/replace\_chain:** To replace the chain with longest chain among the nodes.

[1]: https://github.com/sonusingh99
[2]: https://www.linkedin.com/in/sonu-singh-346988152/ 


---
[![github](https://cloud.githubusercontent.com/assets/17016297/18839843/0e06a67a-83d2-11e6-993a-b35a182500e0.png)][1][![linkedin](https://cloud.githubusercontent.com/assets/17016297/18839848/0fc7e74e-83d2-11e6-8c6a-277fc9d6e067.png)][2]
---

