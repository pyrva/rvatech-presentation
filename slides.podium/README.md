# How to Install Podium on Windows

1. Get Podium (Source code.zip) from: https://github.com/beeware/podium/releases/tag/v0.2.
1. Install briefcase (I just installed right to the system interpreter because it's a build tool):
    ```shell script
    PS C:\...\podium-0.2> pip install briefcase
    ```
1. Build the MSI using briefcase:
    ```shell script
    PS C:\...\podium-0.2> briefcase build
    PS C:\...\podium-0.2> briefcase package
    ```
1. Execute the MSI
1. Wait in anticipation forever
