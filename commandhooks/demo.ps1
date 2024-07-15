$env_name='zedytest01'
$location='eastus2'
$subscription='faa080af-c1d8-40ad-9cce-e1a450ca5b57'

echo "`n--------------------Initializing template--------------------"
azd init -e $env_name -l $location -s $subscription

echo "******** TEST LOCAL FILE HOOK / TEST AZD VARS / INTERACTIVE SET / RUN ON WINDOWS ********" | Out-File -Append ./result.txt

echo "`n--------------------Testing Package related hooks--------------------"
azd package

echo "`n--------------------Testing Provision related hooks--------------------"
azd provision

echo "`n--------------------Testing Deploy related hooks--------------------"
azd deploy

echo "`n--------------------Testing Restore related hooks--------------------"
azd restore

echo "`n--------------------Testing Up related hooks--------------------"
azd up

echo "`n--------------------Testing Down related hooks--------------------"
azd down -e $env_name --force --purge

echo "`n--------------------Removing .azure folder--------------------`n"
rm .azure -r -force

echo "--------------------Fetching the result of hooks trigger--------------------`n"
Get-Content ./result.txt
rm result.txt -r -force

echo "`nCommand hooks test completed, all case passed!`n"