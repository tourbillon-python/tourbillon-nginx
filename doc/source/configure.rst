Configure
*********


Create the tourbillon-nginx configuration file
==============================================

You must create the tourbillon-nginx configuration file in order to use tourbillon-nginx.
By default, the configuration file must be placed in **/etc/tourbillon/conf.d** and its name
must be **nginx.conf**.

The tourbillon-nginx configuration file looks like: ::

	{
		"database": {
			"name": "nginx",
			"duration": "365d",
			"replication": "1"
		},
		"url": "http://localhost/status",
		"frequency": 1,
		"host": "myserver"
	}


You can customize the database name, the retencion policy and the nginx status page url.


Enable the tourbillon-nginx metrics collectors
==============================================

To enable the tourbillon-nginx metrics collectors types the following command: ::

	$ sudo -i tourbillon enable tourbillon.nginx=get_nginx_stats
