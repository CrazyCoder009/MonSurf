import shodan
print("MonSurf is a Web surfing tool that searches for open/vulnerable IP Addresses, ports, webcams, security cameras, satellites and IoT Devices connected over the Internet. Keep in mind that not all features work properly and requires special care, if you emcounter any issues please do share them at the issues sections. Happy Hunting!;) ")
print(" \n")
Shodan_API="syeCnFndQ8TE4qAGvhm9nZLBZOBgoLKd0"
api = shodan.Shodan(Shodan_API)

results=api.search(input("Search for: "))

for result in results['matches']:
        print('IP %s' % result['ip_str'])
        print(result['data'])
		
		#added comment
