`Automated System Update Script for macOS`

Updates macOS system software, Homebrew packages, and `pip` itself.

### Script Creation

1. Open Terminal (vscode, whatever) and navigate to your preferred directory for the script.
2. Use `nano up2date.sh` to create the script file.
3. Enter the following script:

   ```bash
   #!/bin/bash

   echo "Starting system update..."
   softwareupdate -ia --verbose

   echo "Updating Homebrew..."
   brew update && brew upgrade

   echo "Updating pip..."
   pip3 install --upgrade pip```
   
4. Save your script. Since you are using nano, press `Ctrl+O`, `Enter`, then `Ctrl+X` to exit.


Make the script executable: `chmod +x up2date.sh`.

### Script Scheduling with Crontab
![Screenshot 2024-04-01 at 12 47 18 PM](https://github.com/NoDataFound/dotfiles/assets/3261849/01088681-c233-4cca-8ab1-d279387b2d41)

1. Edit your crontab: `crontab -e`
2. Schedule the script for automatic execution, e.g., daily at 3 AM:
```0 3 * * * /absolute/path/to/up2date.sh```

4. Save and exit the crontab editor
5. Verify your new cron job: `crontab -l`

![Screenshot 2024-04-01 at 12 48 21 PM](https://github.com/NoDataFound/dotfiles/assets/3261849/3bbf5c17-c2d9-44e8-90cc-8a9c3a0ee0ad)

### Keep Third party Applications up todate

`I am using https://max.codes/latest/` 
![Screenshot 2024-04-01 at 12 57 25 PM](https://github.com/NoDataFound/dotfiles/assets/3261849/bd99548b-a23c-4cfb-ae24-8bf1b9fb97cf)
