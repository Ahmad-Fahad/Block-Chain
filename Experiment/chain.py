chain = [[1]]

def add_block(transaction_amount):
	chain.append([chain[-1], transaction_amount])
	print(chain)
	#print(chain[-1])

add_block(2)
add_block(3.9)
add_block(4.9)

