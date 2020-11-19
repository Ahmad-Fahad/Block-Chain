chain = [1]

def add_block():
	chain.append([chain[0], 5.4])
	print(chain)

add_block()
add_block()
add_block()