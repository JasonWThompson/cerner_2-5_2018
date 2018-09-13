# CompetitionReminder.ps1
# Author: Jason W. Thompson
# Commentary: Powershell is my favorite scripting language in the world. It is far more legible than bash and has
# access to COM and .NET objects installed on the system. As such, one can do some fairly powerful stuff with just a
# little bit of code. This small program automates adding a task to outlook to remind me to author and publish an entry
# for the 2^5th competion. All I need to do now is set this up as a scheduled task.

# I used the following site as a source to figure out how to do this:
# http://www.leeholmes.com/blog/2007/03/01/getting-things-done-outlook-task-automation-with-powershell/

$outlook = New-Object -Com Outlook.Application 
$task = $outlook.Application.CreateItem(3) 
$task.Subject = "Don't forget to submit your cerner_2^5_2018 entry for the day!"
$task.Save() 
$outlook = $null
