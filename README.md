# OLGA License Checker

This is a simple Python script which queries the OLGA servers in your organization and checks for license availability of any particular module/feature. Why create this script?
  - The SLB licensing tool queries all servers for all modules which can be time consuming and the information outputted might not be up to date
  - Aren't simple scripts which you can run on your terminal just more fun?

# Requirements

  - This script requires a copy of lmutil.exe in it's working directory. If you have OLGA installed on your machine, search for lmutil.exe to find it
  - The script itself needs all the server addresses for the modules you want to check. You will need to populate the empty "servers" list inside the script

### Todos

 - Output names of users currently using a license

License
----

MIT