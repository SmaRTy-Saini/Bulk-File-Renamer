# Define a function to rename files
function Rename-Files {
    param (
        [string]$folderPath,
        [string]$prefix,
        [string]$dateFormat
    )

    if (-not (Test-Path $folderPath)) {
        Write-Host "Folder not found!" -ForegroundColor Red
        return
    }

    $files = Get-ChildItem -Path $folderPath -File
    if ($files.Count -eq 0) {
        Write-Host "No files found in the folder!" -ForegroundColor Red
        return
    }

    $counter = 1
    foreach ($file in $files) {
        $extension = $file.Extension
        $newName = if ($dateFormat) {
            $date = Get-Date -Format $dateFormat
            "$prefix" + "_" + "$date" + "_" + $counter + $extension
        } else {
            "$prefix" + "_" + $counter + $extension
        }

        $newFilePath = Join-Path $folderPath $newName
        Rename-Item -Path $file.FullName -NewName $newFilePath
        $counter++
    }

    Write-Host "Renamed $($files.Count) files successfully!" -ForegroundColor Green
}

# Ask user for inputs
$folderPath = Read-Host "Enter the folder path"
$prefix = Read-Host "Enter the prefix for the files"
$dateFormat = Read-Host "Enter the date format (optional, e.g., yyyy-MM-dd)"

# Call the Rename-Files function
Rename-Files -folderPath $folderPath -prefix $prefix -dateFormat $dateFormat
