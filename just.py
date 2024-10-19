import subprocess

# Get all the profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='backslashreplace').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Loop through each profile and get the password
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    password = None
    for line in results:
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            break

    # Print profile name and password or "None" if no password is found
    if password:
        print("{:<30}| {:<}".format(profile, password))
    else:
        print("{:<30}| {:<}".format(profile, "None"))

input("\n\nPress enter to continue...")
