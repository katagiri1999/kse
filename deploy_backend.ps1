$ErrorActionPreference = "Stop"

try {
    Write-Host "- Start Backend Deploy" -ForegroundColor Green

    $check = Read-Host "This is prod. Are You Sure? (y/n)"
    if ($check -ne "y") {
        throw "Stop Deploy"
    }

    # set location to this script dir
    Set-Location $PSScriptRoot

    # aws configure
    $credential = Get-Content "~/credential.yaml" | ConvertFrom-Yaml
    $env:AWS_ACCESS_KEY_ID = $credential.aws.iam.access_key_id
    $env:AWS_SECRET_ACCESS_KEY = $credential.aws.iam.secret_access_key
    $env:AWS_DEFAULT_REGION = $credential.aws.iam.region

    # set config file
    Set-Location lambda-kse
    Write-Host "- Set config file" -ForegroundColor Yellow
    cp ./config/config_prod.py ./sub/config.py

    # remove cache files
    Write-Host "- Cache clear" -ForegroundColor Yellow
    Get-ChildItem *.pyc -Recurse | Remove-Item

    # package
    Write-Host "- Package" -ForegroundColor Yellow
    Compress-Archive -Path ./* -DestinationPath zip.zip -f

    # deploy
    Write-Host "- Deploy" -ForegroundColor Yellow
    aws lambda update-function-code --function-name kse-api-prod --zip-file fileb://zip.zip

    Write-Host "- Successfully Deployed" -ForegroundColor Green

} catch {
    Write-Host $Error[0] -ForegroundColor Red
    Write-Host $PSItem.ScriptStackTrace -ForegroundColor Red

} finally {
    Set-Location $PSScriptRoot
    cp ./lambda-kse/config/config_dev.py ./lambda-kse/sub/config.py
}
