# Define variables
$sourceBranch = "main"
$destinationBranch = "release"
$fileToCheck = "hello.py"

Write-Host "Source Branch: $sourceBranch"
Write-Host "Destination Branch: $destinationBranch"
Write-Host "File to Check: $fileToCheck"

$doesFileExist = git show ${sourceBranch}:${fileToCheck} 2>$null
Write-Host "File Existence Check Result: $doesFileExist"

if ($doesFileExist) {
    Write-Host "Checking out $destinationBranch..."
    git checkout $destinationBranch

    Write-Host "Merging changes from $sourceBranch..."
    git merge $sourceBranch

    Write-Host "Pushing changes to $destinationBranch..."
    git push origin $destinationBranch

    Write-Host "Switching back to $sourceBranch..."
    git checkout $sourceBranch

    Write-Host "Changes successfully pushed to $destinationBranch."
} else {
    Write-Host "$fileToCheck does not exist in $sourceBranch branch."
}
