def scan_nfs(config_file="tmp/exports"):
    import os
    import re
    
    print("Scanning NFS configuration for dangerous settings...")
    
    # Define dangerous settings to look for
    dangerous_settings = {
        "rw": "Read and write permissions",
        "insecure": "Ports above 1024 will be used",
        "nohide": "If another file system was mounted below an exported directory, this directory is exported by its own exports entry",
        "no_root_squash": "All files created by root are kept with the UID/GID 0"
    }
    
    # Check if the config file exists
    if not os.path.exists(config_file):
        print(f"Warning: {config_file} does not exist. NFS may not be installed.")
        return
    
    # Read the configuration file
    try:
        with open(config_file, 'r') as f:
            config_lines = f.readlines()
    except Exception as e:
        print(f"Error reading {config_file}: {e}")
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
        
        # Extract the export path and options
        parts = line.split(None, 1)
        if len(parts) < 2:
            continue
            
        export_path = parts[0]
        options_part = parts[1]
        
        # Process each client and its options
        client_options = re.findall(r'([^\s(]+)(?:\(([^)]*)\))?', options_part)
        
        for client, options in client_options:
            if not options:
                continue
                
            # Check each option against dangerous settings
            option_list = options.split(',')
            for option in option_list:
                option = option.strip()
                if option in dangerous_settings:
                    print(f"- {export_path} exported to {client} with {option}: {dangerous_settings[option]}")
                    dangerous_found = True
    
    if not dangerous_found:
        print("No dangerous settings found in NFS configuration.")
    return