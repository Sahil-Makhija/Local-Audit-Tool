def scan_ftp(config_path="/etc/vsftpd.conf"):
    import os
    import re
    
    print("Scanning FTP configuration for dangerous settings...")
    
    # Define dangerous settings to look for
    dangerous_settings = {
        "anonymous_enable=YES": "Allowing anonymous login",
        "anon_upload_enable=YES": "Allowing anonymous to upload files",
        "anon_mkdir_write_enable=YES": "Allowing anonymous to create new directories",
        "no_anon_password=YES": "Not asking anonymous for password",
        "write_enable=YES": "Allowing usage of FTP commands: STOR, DELE, RNFR, RNTO, MKD, RMD, APPE, and SITE",
    }
    
    # Also check for anon_root setting
    anon_root_pattern = re.compile(r"anon_root\s*=\s*(.+)")
    
    # Check if the config file exists
    if not os.path.exists(config_path):
        print(f"Warning: {config_path} does not exist. vsftpd may not be installed.")
        return
    
    # Read the configuration file
    try:
        with open(config_path, 'r') as f:
            config_lines = f.readlines()
    except Exception as e:
        print(f"Error reading {config_path}: {e}")
        return
    
    # Initialize a flag to track if any dangerous settings were found
    dangerous_found = False
    
    # Check for dangerous settings
    print("\nDangerous settings found:")
    for line in config_lines:
        line = line.strip()
        
        # Skip comments and empty lines
        if not line or line.startswith('#'):
            continue
        
        # Check for dangerous settings
        for setting, description in dangerous_settings.items():
            if line.lower() == setting.lower():
                print(f"- {setting}: {description}")
                dangerous_found = True
        
        # Check for anon_root setting
        anon_root_match = anon_root_pattern.match(line)
        if anon_root_match:
            anon_root_value = anon_root_match.group(1)
            print(f"- anon_root={anon_root_value}: Directory for anonymous access")
            dangerous_found = True
    
    if not dangerous_found:
        print("No dangerous settings found in vsftpd configuration.")
    return