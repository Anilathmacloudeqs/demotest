# Define variables
$sourceBranch = "main"
$destinationBranch = "release"
$fileToCheck = "hello.py"

# Check if the file exists in the source branch
$doesFileExist = git show ${sourceBranch}:${fileToCheck} 2>$null

if ($doesFileExist) {
    # Checkout the release branch
    git checkout $destinationBranch

    # Merge the changes from the source branch
    git merge $sourceBranch

    # Push changes to the release branch
    git push origin $destinationBranch

    # Switch back to the original branch
    git checkout $sourceBranch

    Write-Host "Changes successfully pushed to $destinationBranch."
} else {
    Write-Host "$fileToCheck does not exist in $sourceBranch branch."
}
