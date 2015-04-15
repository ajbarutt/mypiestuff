import json

def main():
	F = open("test.json", 'r')
	Data = F.read()
	F.close()
	JData = json.loads(Data)

	JData["Lname"] = "Smith"

	JData["Computers"]["Windows"] = ""
	
	F = open("output.json", 'w')

	json.dump(JData, F)

	print JData

if __name__ == "__main__":
	main()