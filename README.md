# ds-alert
A script that connects to Synology Download Station and returns all torrents that have failed trackers.

You can use this script to identify torrents that you are seeding but are unregistered.

## How to run
Variables to set:
- **BASE_URL:** http://SYNOLOGY_ADDRESS:5000/webapi/
- **USERNAME:** Your Synology user

## Other Info
[Based on Synology's API Docs](https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/DownloadStation/All/enu/Synology_Download_Station_Web_API.pdf
)