<#This scripts will add servers in respective collection provided in CSV

Example: 


servername,collection
abc,coll1
bcd,coll1
cde,coll2
it will add abc,bcd in coll1 and cde in coll2

Created By Mukesh Lohar
#>

$file = import-csv -path "C:\2021_Mukesh\test.csv" -Delimiter ',' #provide csv in header as servername,collection

foreach($line in $file){
Write-Host "Adding" $line.servername "to" $line.collection -ForegroundColor Green

$deviceid = Get-CMDevice -Name $line.servername

Add-CMDeviceCollectionDirectMembershipRule -CollectionName $line.collection -ResourceID $deviceid.ResourceID -Verbose -ErrorAction SilentlyContinue



}

