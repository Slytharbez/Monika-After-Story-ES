$jsonDir = "c:\Users\Admin\Desktop\MAS 7.8.4\Monika-After-Story-Android-ES\Monika After Story Android\game\mod_assets\monika\j"
$hairDir = "c:\Users\Admin\Desktop\MAS 7.8.4\Monika-After-Story-Android-ES\Monika After Story Android\game\mod_assets\monika\h"

# Get all JSON files
$jsons = Get-ChildItem -Path $jsonDir -Filter "*.json"

foreach ($jFile in $jsons) {
    $content = Get-Content $jFile.FullName -Raw | ConvertFrom-Json
    
    # Check if it is a hair file (Type 1 or specific group)
    if ($content.type -eq 1) {
        Write-Host "Processing $($jFile.Name)..."
        
        # 1. Update JSON Content
        $changed = $false
        
        # Force numeric layer IDs
        if (-not $content.psObject.Properties['use_numeric_layer_ids']) {
            $content | Add-Member -Type NoteProperty -Name "use_numeric_layer_ids" -Value $true
            $changed = $true
        }
        elseif ($content.use_numeric_layer_ids -ne $true) {
            $content.use_numeric_layer_ids = $true
            $changed = $true
        }
        
        # Fix img_sit path (remove h/ prefix if present)
        if ($content.img_sit -like "h/*") {
            $content.img_sit = $content.img_sit.Substring(2)
            $changed = $true
            Write-Host "  Fixed img_sit path."
        }
        
        if ($changed) {
            $content | ConvertTo-Json -Depth 10 | Set-Content $jFile.FullName
            Write-Host "  Updated JSON."
        }
        
        # 2. Process Image Folders
        $targetFolders = @()
        $baseName = $content.img_sit
        
        # Main folder
        $targetFolders += Join-Path $hairDir $baseName
        # Leaning folder (standard naming convention)
        $targetFolders += Join-Path $hairDir ("leaning-def-" + $baseName)
        
        foreach ($folder in $targetFolders) {
            if (Test-Path $folder) {
                Write-Host "  Checking folder: $folder"
                
                # A. Rename back/front to 0/10 if strictly text-based
                # Note: We prioritize numeric. If 0.png doesn't exist but back.png does, rename it.
                
                if ((Test-Path "$folder\back.png") -and (-not (Test-Path "$folder\0.png"))) {
                    Rename-Item "$folder\back.png" "0.png"
                    Write-Host "    Renamed back.png -> 0.png"
                }
                if ((Test-Path "$folder\front.png") -and (-not (Test-Path "$folder\10.png"))) {
                    Rename-Item "$folder\front.png" "10.png"
                    Write-Host "    Renamed front.png -> 10.png"
                }
                
                # B. Create def- copies
                if ((Test-Path "$folder\0.png") -and (-not (Test-Path "$folder\def-0.png"))) {
                    Copy-Item "$folder\0.png" "$folder\def-0.png"
                    Write-Host "    Created def-0.png"
                }
                if ((Test-Path "$folder\10.png") -and (-not (Test-Path "$folder\def-10.png"))) {
                    Copy-Item "$folder\10.png" "$folder\def-10.png"
                    Write-Host "    Created def-10.png"
                }
            }
        }
    }
}

Write-Host "Done."
