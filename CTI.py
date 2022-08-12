import os


# Check to see if directory exist. If directory doesn't exist create it.

CTI_dir = os.path.expanduser('~/Documents/CTI_Report')
check_folder = os.path.isdir(CTI_dir)

if not check_folder:
    os.makedirs(CTI_dir)
    print('Created Directory... all results will be saved in: ', CTI_dir)
else:
    print('All results will be logged in : ', CTI_dir)


print('Enter domain to search for cyber threat intelligence: ')
domain = input()

def permutations():
    # dnstwist to search for domain permutaitons and save output to file.

    print('Now commencing dnstwist for ' + domain)  
    os.system('dnstwist -o ~/Documents/CTI_Report/dnstwist.output -r ' + domain )
    print('dnstwist complete.')
    print('Now commencing to dig permutations')

def digPermutations():
    # dig found permutations to lookup DNS records and save output to file.

    os.system('dig -f ~/Documents/CTI_Report/dnstwist.output any > ~/Documents/CTI_Report/dig_dnstwist.output')
    print('Permutations dig complete. ')
    print('Now commencing Shodan domain lookup for ' + domain)


def shodan():
    # Run shodan for all avialble information on a domain and save outout to file.
    
    os.system('shodan domain ' + domain + ' > ~/Documents/CTI_Report/shodan.output ')
    print('Shodan domain look up complete. ')
    print('Now commencing amass subdomain discovery for ' + domain)

def amass():
  # Run amass to find and list all subdomains. Save output to file.

  os.system('amass enum -o ~/Documents/CTI_Report/amass.output -ip -d ' + domain + ' -src ')
  print('amass complete. ')
  print('Now Commencing to dig subdomains...')

def digSubdomains():
  # dig found subdomains and save output to file.

  os.system('dig -f ~/Documents/CTI_Report/amass.output > dig_amass.output')
  print('amass dig complete.')
  print('Now commencing EmailHarvester for ' + domain)

def emailHarvester():
  # Retrieve domain email addresses from search engines 
  os.system('EmailHarvester -s ~/Documents/CTI_Report/EmailHarvester.output -d ' + domain)
  print('EmailHarvester complete')


permutations()
digPermutations()
shodan()
amass()
digSubdomains()
emailHarvester()
print('CTI gathering complete! Go to ' + CTI_dir + ' to see outputs' )
