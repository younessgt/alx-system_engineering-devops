

# Postmortem: Web Stack Debugging Project - Internal Server Error Outage




### Issue Summary:

Duration of the Outage : The outage occurred from 10:00 AM to 12:30 PM GMT on November 7, 2023.
Impact : When users tried to visit our website, they kept getting the error "500 Internal Server Error." This problem affected almost 75% of our users, which caused a major disruption in their ability to use our services.
Root Cause: A typographical issue in the wp-settings.php file, where a filename extension was misspelled as “.phpp” instead of the correct “.php” , this was found to be the main cause.

### Timeline:

* 10:00 AM GMT: Problem was initially identified through user complaints about the 500 error
* 10:15 AM GMT: Initial assumption was a server configuration error. Netstat checks confirmed normal port listening.
* 10:50 AM GMT: Error log files reviewed, nothing out of the ordinary.
* 11:00 AM GMT: The strace tool was used to find a misspelled filename in the wp-settings.php file.
* 11:30 AM GMT: Corrective action taken to fix the filename typo.
* 12:00 PM GMT: Website restored to full functionality. Deployment of a Puppet script across all servers to prevent similar issues.

### Root Cause and Resolution:

Root Cause: The outage was caused by a simple typographical error in the wp-settings.php file, where a file extension was spelled incorrectly. The 500 error was caused by the server's inability to locate the required file.

Resolution: The problem was resolved by changing the file extension from.phpp to.php. To guarantee consistency among all servers, a Puppet script was run to automatically fix comparable mistakes in other places.

### Corrective and Preventative Measures

Improve monitoring systems to detect and alert unusual server responses like 500 errors.
Ensure that all code changes are thoroughly reviewed by multiple team members before deployment.
Integrate automated tools to scan for common errors like typos in critical configuration files.

