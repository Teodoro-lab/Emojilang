import re

stack = []

def P(string):
	string = re.sub(r'\s', "", string)
	stack.append("#")
	Q(string)


def Q(string):
	# e / <>... <= ... >= ... < ... > / BOOLEAN
	if stack[-1] in ('<>', '<=', '>=', '<', '>'):
		del(stack[-1])
		stack.append("BOOLEAN")
		Q(string)

	# e / 1..2..3.. / NUMBER
	elif stack[-1] in ('1️⃣','2️⃣','3️⃣','4️⃣') or stack[-1].isdigit():
		del(stack[-1])
		stack.append("NUMBER")
		Q(string)

	# e / "'hola mundus!'" / STRING
	elif stack[-1] == "'holamundus!'":
		del(stack[-1])
		stack.append("STRING")
		Q(string)

	# e / )NUMBER BOOLEAN NUMBER( / CONDITION
	elif "".join(stack[-5:]) == "(NUMBERBOOLEANNUMBER)":
		del(stack[-5:])
		stack.append("CONDITION")
		Q(string)

	# e / STRING🖨 / BODY
	elif "".join(stack[-2:]) == "🖨STRING":
		del(stack[-2:])
		stack.append("BODY")
		Q(string)

	# e / IF_STAT / BODY
	elif "".join(stack[-1]) == "IF_STAT":
		del (stack[-1])
		stack.append("BODY")
		Q(string)

	# e / !BODY👉CONDITION❓ / IF_STAT
	elif "".join(stack[-5:]) == "❓CONDITION➡BODY❗":
		del(stack[-5:])
		stack.append("IF_STAT")
		Q(string)

	# e / ⏹ IF_STAT ▶ / PROGRAM
	elif "".join(stack[-3:]) == "▶IF_STAT⏹":
		del(stack[-3:])
		stack.append("PROGRAM")
		Q(string)

	elif "".join(stack[-3:]) == "▶BODY⏹":
		del(stack[-3:])
		stack.append("PROGRAM")
		Q(string)

	# ⏹ / e / ⏹
	elif string != "" and string[0] == "⏹":
		stack.append(string[0])
		string = string.lstrip("⏹")
		Q(string)

	# ▶ / e / ▶
	elif string != "" and string[0] == "▶":
		stack.append(string[0])
		string = string[1:]
		Q(string)

	# ) / e / )
	elif string != "" and string[0] == ")":
		stack.append(string[0])
		string = string[1:]
		Q(string)
	
	# ( / e / (
	elif string != "" and string[0] == "(":
		stack.append(string[0])
		string = string[1:]
		Q(string)

	# ❓ / e / ❓
	elif string != "" and string[0] == "❓":
		stack.append(string[0])
		string = string[1:]
		Q(string)
		
	# 👉 / e / 👉
	elif string != "" and string[0] == "➡":
		stack.append(string[0])
		string = string[1:]
		Q(string)

	# ❗ / e / ❗
	elif string != "" and string[0] == "❗":
		stack.append(string[0])
		string = string[1:]
		Q(string)

	# 🖨️ / e / 🖨️
	elif string != "" and string[0] == "🖨":
		stack.append(string[0])
		string = string[1:]
		Q(string)
	
	# '<>', '<=', '>=', '<', '>' / e / '<>', '<=', '>=', '<', '>'
	elif string != "" and (string[0:2] in ('<>', '<=', '>=') or string[0] in ('<', '>')):
		stack.append('<')
		string = string[1:]
		Q(string)
	
	# ('1️⃣','2️⃣','3️⃣','4️⃣') / e / ('1️⃣','2️⃣','3️⃣','4️⃣')
	elif string != "" and (string[0] in ('1️⃣','2️⃣','3️⃣','4️⃣') or string[0].isdigit()):
		stack.append(string[0])
		string = string[1:]
		Q(string)
	
	elif string.startswith("'holamundus!'"):
		stack.append("'holamundus!'")
		string = string[len("'holamundus!'"):]
		Q(string)

	else:
		F(string)

def F(string):
	if stack == ['#', 'PROGRAM'] and string == "":
		print("Successful compilation")
		return 0
	print("Compilation failed")
	return 1
	



