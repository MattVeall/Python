import os

def CTI_Directory():
    # Check to see if directory exist. If directory doesn't exist create it.

    CTI_dir = os.path.expanduser('~/Documents/CTI_Report')
    check_folder = os.path.isdir(CTI_dir)

    if not check_folder:
        os.makedirs(CTI_dir)
        print('Created Directory, all results will be saved in :', CTI_dir)
    else:
        print('All results will be logged in : ', CTI_dir)


def permutations():
    # dnstwist to search for domain permutaitons and save output to file.
      
    print('Enter domain to search for permutations: ')
    website = input()   
    os.system('dnstwist -o ~/Documents/CTI_Report/dnstwist_output -r ' + website )
    print('dnstwist complete... now commencing to dig permutations')

def digDNS():
    # dig to lookup DNS records
    os.system('dig -f ~/Documents/CTI_Report/dnstwist_output any > ~/Documents/CTI_Report/dig_output')

CTI_Directory()
permutations()
digDNS()
