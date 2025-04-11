from args_parser import parse_arguments
from protocols.switch import switch

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # If 'all' is specified, scan all protocols
    if args.protocols == ['all']:
        protocols_to_scan = ['ftp', 'smb', 'nfs', 'dns', 'smtp', 'imap', 'pop3', 
                           'snmp', 'mysql', 'mssql', 'oracle_tns', 'ipmi']
    else:
        protocols_to_scan = args.protocols
    
    # Process each protocol
    for protocol in protocols_to_scan:
        # Scans any dangerous settings available for the protocol
        switch(protocol)


if __name__ == "__main__":
    main()
