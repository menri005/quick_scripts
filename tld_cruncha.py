import dns.resolver

teams = ['elbocon']

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

results_dict = {}

with open('tlds.txt', 'r') as f:
    for team in teams:
        print('Resolving domain name for {}. Please wait.'.format(team))
        
        for tld in f:
            domain_name = '{}.{}'.format(team, tld)
            
            # strip leading whitepaces from reading text file
            domain_name = domain_name.strip()

            try:
                result = resolver.resolve(domain_name, 'A')
                ip_address = result[0].to_text()
                results_dict[domain_name] = ip_address
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, KeyError):
                pass
                
with open('dns_results.txt', 'w') as f:
    for key, value in results_dict.items():
        f.write('{}:{}\n'.format(key, value))
                
               
            
        
