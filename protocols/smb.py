def scan_smb(config_file="/etc/samba/smb.conf"):
    import os
    import re
    
    print("Scanning SMB configuration for dangerous settings...")
    
    # Define dangerous settings to look for
    dangerous_settings = {
        "browseable = yes": "Allowing listing available shares in the current share",
        "read only = no": "Allowing creation and modification of files",
        "writable = yes": "Allowing users to create and modify files",
        "guest ok = yes": "Allowing connections without password",
        "enable privileges = yes": "Honoring privileges assigned to specific SID",
        "create mask = 0777": "Assigning full permissions to newly created files",
        "directory mask = 0777": "Assigning full permissions to newly created directories",
        "logon script": "Script executed on user login",
        "magic script": "Script executed when the script gets closed",
        "magic output": "Output location for magic script"
    }
    
    # Check if the config file exists
    if not os.path.exists(config_file):
        print(f"Warning: {config_file} does not exist. Samba may not be installed.")
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
    
    # Filter out comment lines and empty lines
    filtered_lines = []
    for line in config_lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith(';'):
            filtered_lines.append(line)
    
    # Check for dangerous settings
    print("\nDangerous settings found:")
    current_share = "Global"
    
    for line in filtered_lines:
        # Check if this is a share definition
        if line.startswith('[') and line.endswith(']'):
            current_share = line[1:-1]
            continue
        
        # Check for dangerous settings
        for setting, description in dangerous_settings.items():
            # For settings that need exact match
            if setting in ["browseable = yes", "read only = no", "writable = yes", 
                          "guest ok = yes", "enable privileges = yes", 
                          "create mask = 0777", "directory mask = 0777"]:
                if line.lower() == setting.lower():
                    print(f"- [{current_share}] {setting}: {description}")
                    dangerous_found = True
            # For settings that need partial match
            else:
                setting_name = setting.split()[0]
                if line.lower().startswith(f"{setting_name} = "):
                    value = line.split('=', 1)[1].strip()
                    print(f"- [{current_share}] {setting_name} = {value}: {description}")
                    dangerous_found = True
    
    if not dangerous_found:
        print("No dangerous settings found in Samba configuration.")
    return