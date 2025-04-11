import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Python Script to scan any `Dangerous` settings enabled on system.")
    
    # Add protocol argument with support for multiple protocols
    parser.add_argument('protocols', 
                       nargs='+',
                       choices=['ftp', 'smb', 'nfs', 'dns', 'smtp', 'imap', 'pop3', 
                               'snmp', 'mysql', 'mssql', 'oracle_tns', 'ipmi', 'all'],
                       help='Protocol(s) to scan for dangerous settings')
    
    # Add optional argument for FTP configuration file 
    # TODO: Add support for this arg
    parser.add_argument('--ftp_config_file',
                       type=str,
                       default='/etc/vsftpd.conf',
                       help='Path to the FTP configuration file (default: /etc/vsftpd.conf)')

    args = parser.parse_args()
    
    # If 'all' is present with other protocols, just use 'all'
    if 'all' in args.protocols:
        if len(args.protocols) > 1:
            print("Warning: 'all' specified with other protocols. Using 'all' only.")
        args.protocols = ['all']
    
    return args