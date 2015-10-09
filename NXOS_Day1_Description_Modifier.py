from cli import *

def setDescription(interfaces,switch_name):
	for interface in interfaces:
		cli("conf ; interface " + interface+" ; description " + switch_name + " " + interface)
		
def ensureIntegrity(interfaces,switch_name):
	config_integrity = {}
	for interface in interfaces:
		config_integrity[interface] = switch_name + " " + interface
	for key,value in config_integrity.iteritems():
		test = json.loads(clid("show interface "+key))
		data = test['TABLE_interface']['ROW_interface']
		if value != data['desc']:
			print key+ "  does not have the correct description\n"
			print "Fixing...\n"
			fixinterface=[key]
			setDescription(fixinterface,switch_name)
	print "Done!"



def main():
	interfaces = ["Ethernet 1/1", "Ethernet 1/2", "Ethernet 1/3", "Ethernet 1/4", "Ethernet 1/5"]
	switch_name= "Bob"
	print "What would you like to do: \n"
	print "1. Set Initial Descriptions"
	print "2. Ensure Integrity of Descriptions\n"

	choice= raw_input()
	print "\n"

	if int(choice) == 1:
		setDescription(interfaces,switch_name)
		print "Successfuly changed interface descriptions"
	elif int(choice) == 2:
		ensureIntegrity(interfaces,switch_name)
	else:
		print "Well you chose the wrong number"



if __name__ == "__main__":
	main()