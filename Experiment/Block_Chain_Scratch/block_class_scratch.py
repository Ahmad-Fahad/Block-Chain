from flask import Flask
from flask import request
import json
import requests
import hashlib as hasher
import datetime as date
node = Flask(__name__)

class Block:
	def __init__(self, index, time_stamp, data, previous_hash):
		self.index         = index
		self.time_stamp    = time_stamp
		self.data 		   = data
		self.previous_hash = previous_hash
		self.hash 		   = self.hash_block()

	def hash_block(self):
		sha = hasher.sha256()
		sha.update(self.attributes())
		return sha.hexdigest()

	def attributes(self):
		return str(self.index) + str(self.time_stamp) + str(self.data) + str(self.previous_hash)

	def create_genesis_block():
		return Block(0, date.datetime.now(), {
			"proof-of-work" : 9,
			"transactions"  : None,
			}, "0")

	def proof_of_work(last_proof):  # Not cleared
		incrementor = last_proof+1
		while not(incrementor%9 == 0 and incrementor%last_proof == 0):
			incrementor += 1
		return incrementor

	def update_block_chain(src):
		if len(src) <= len(block_chain)
			return block_chain
		ret = []
		for b in src:
			ret.append(Block(b['index'], b['time_stamp'], b['data'], b['hash']))
		return ret

	def find_other_chains():
		ret = []
		for peer in peer_nodes:
			response = requests.get('http://%s/blocks'%peer)
			if response.status_code == 200:
				print("blocks from peer: "+response.content)
				ret.append(json.loads(response.content))
		return ret

	def consensus():
		global block_chain
		longest_chain = block_chain
		for chain in find_other_chains():
			if len(longest_chain) < len(chain):
				longest_chain = chain
		return update_block_chain(longest_chain)


miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"
block_chain    = []
peer_nodes    = []
mining        = True
transactions  = []


@node.route('/transaction', methods = ['POST'])
def transaction():
	if request.method == 'POST'
	transaction  = request.get_json()
	transactions.append(transaction)
	print("New Transaction")
	print(f"From: {transaction['from']}")
	print(f"To: {transaction['to']}")
	print(f"Amount: {transaction['amount']}")
	return "Transaction Submission Successful"

@node.route('/blocks', methods=['GET'])
def get_blocks():
	ret = []
	for block in consensus():
		ret.append({
			"index":str(block.time_stamp),
			"time_stamp":str(block.time_stamp),
			"data":str(block.data),
			"hash":block.hash
			})
	return json.dumps(ret)

@node.route('/add_user', methods=['GET'])
def add_peer():
	host = request.args['hsot'] if 'host' in request.args else 'localhost'
	port = request.args['port']
	peer = host+':'+port
	peer_nodes.append(peer)
	print("Peer Added:%s"%peer)
	return ""


@node.route('/mine', methods=['GET'])
def mine():
	last_block = block_chain[len(block_chain) - 1]
	last_proof = last_block.data['proof-of-work']
	proof = proof_of_work(last_proof)
	transactions.append({
		"from":"network",
		"to":miner_address,
		"amount":1
		})
	data = {
		"proof-of-work":proof,
		"transactions":list(transactions)
	}
	index = last_block.index+1
	time_stamp = data.datetime.now()
	transactions[:] = []
	block = Block(index, time_stamp, data, last_block.hash)
	block_chain.append(block)
	return json.dumps({
		"index":index,
		"time_stamp":str(time_stamp),
		"data":data,
		"hash":last_block.hash
		})+ "\n"

def main():
	port = 5000
	if len(sys.argv)>1:
		port = sys.argv[1]
	block_chain.append(create_genesis_block())
	node.run(port=port)

if __name__ == "__main__":
	main()



