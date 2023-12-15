name: Push to Release

on:
  push:
    branches:
      - main

jobs:
  push_to_release:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run PowerShell script
        run: |
          $ErrorActionPreference = 'Stop'
          pwsh -File push-to-release.ps1
