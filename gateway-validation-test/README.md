# Project Documentation

## List of Environment Variables
- `"LE_GATEWAY_VLDN_USERNAME_TOKEN`
- `LE_GATEWAY_VLDN_HOST_IP_ADDRESS`
- `LE_SSH_USERNAME`
- `LE_SSH_PASSWORD`


## List of Associated Files
### Python Files:
1. wrapper_validn.py: Main wrapper file for executing the Gateway validation test sequentially and generate report skeleton file in word
2. standalone_ssh_restart.py : File to restart elements of LE

### Other files
1. devices_and_tags_template.json: for devices and tags
2. flows_template.json: for flows template
3. analytics_default_export.json : optional analyics template file (not currently used in the code as the process is being done manually)

## Brief Information about Generated Files
1. gateway_validation_report.docx: A template of the gateway validation report, with entries to be filled manually as per the specific gateway being tested and for results

## Libraries Used
- `requests`
- `urllib3`

## Steps Before Execution
1. Make sure to install the required libraries
2. Access the API token and other authorizations post installing LE on the gateway


## Running the Code
1. The test is excuted by running the 'wrapper_validn.py' file to generate the reports and doing the necessary processes for testing
2. Carefully observe the terminal messages to troubleshoot or analyse the progress if required.

## Additional Points
1. The code doesnt't generate screenshots of the required webpages. One can incorporate that feature after each step of the process and by putting proper delays after each part.
2. The results can be linked with the response message being obatined from the server (for example: 200 or 204 can be test result is good combined with good CPU levels)
3. For the OPC UA part, the code creates a hierarchy, starts the server and imports nodes but the client side feature (i.e with UAExpert or SSH) is not yet implemented
