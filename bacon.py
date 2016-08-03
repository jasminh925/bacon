def bacon():
	pork = raw_input("Should you eat that bacon?")
	angels = raw_input("Do you want to feel like angels are frolicking on your taste buds?").lower()
	if angels == "yes":
		return "Eat it!"
	elif angels == "no":
		print "You've clearly never tasted bacon."
		return "Eat it"
	else:
		coward = raw_input("I see you are afraid bacon might kill you. Are you a coward?").lower()
		if coward == "yes":
			return "You are a coward. Bacon will turn you into a true warrior."
		else:
			return "Then eat it!"



def main():
	print bacon()

if __name__ == '__main__':
	main()