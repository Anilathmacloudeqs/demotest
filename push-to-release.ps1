# push-to-release.ps1

$sourceBranch = "main"
$destinationBranch = "release"
$fileToCheck = "hello.py"

Write-Host "Source Branch: $sourceBranch"
Write-Host "Destination Branch: $destinationBranch"
Write-Host "File to Check: $fileToCheck"

# Check if the file exists
if (Test-Path $fileToCheck) {
    Write-Host "File Existence Check Result: $($fileToCheck | Get-Content)"
    
    # Checkout or create the 'release' branch
    git checkout $destinationBranch 2>$null
    if ($?) {
        Write-Host "Checking out $destinationBranch..."
    } else {
        Write-Host "Creating and checking out $destinationBranch..."
        git checkout -b $destinationBranch
    }

    # Merge changes from the 'main' branch
    git merge $sourceBranch

    # Push changes to 'release'
    git push origin $destinationBranch

    Write-Host "Changes successfully pushed to $destinationBranch."

    # Switch back to 'main'
    git checkout $sourceBranch
    Write-Host "Switching back to $sourceBranch..."
} else {
    Write-Host "File $fileToCheck not found."
}
