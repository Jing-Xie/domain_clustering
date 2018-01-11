# domain_clustering

* Install python virtualenv if not yet done so
`$ pip install virtualenv`

* clone this repo and cd to it, and then activate your virtualenv
`$ virtualenv .`

* Install dependency libraries
`$ pip install -r requirements.txt`

* Run the following command
`$ cat input_v.tsv | python map.py | sort -k1,1 | python reduce.py`


You should be able to see results that similar to this:

`
Cluster #  0
mailserv.venafi.com

Cluster #  1
www1windows.venafi.com
www2windows.venafi.com
www3windows.venafi.com

Cluster #  2
ftpserv.venafi.com

Cluster #  3
vpnserv.venafi.com

Cluster #  4
www1linux.venafi.com
www2linux.venafi.com
www3linux.venafi.com
`
